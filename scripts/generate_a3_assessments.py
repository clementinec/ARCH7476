#!/usr/bin/env python3
import os
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
A3_DIR = ROOT / 'A3'
OUT_QMD = A3_DIR / 'A3-assessments.auto.qmd'

def read_text_from_pdf(path: Path) -> str:
    try:
        res = subprocess.run(['pdftotext', '-layout', '-nopgbrk', '-enc', 'UTF-8', str(path), '-'],
                             check=True, capture_output=True)
        return res.stdout.decode('utf-8', errors='ignore')
    except Exception:
        return ''

def read_text_from_docx(path: Path) -> str:
    try:
        res = subprocess.run(['pandoc', str(path), '-t', 'markdown'], check=True, capture_output=True)
        return res.stdout.decode('utf-8', errors='ignore')
    except Exception:
        return ''

def read_text_from_txt(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return ''

def read_text_from_pptx(path: Path) -> str:
    # Extract text using the same approach as pptx_to_rtf
    import zipfile
    import xml.etree.ElementTree as ET
    texts = []
    try:
        with zipfile.ZipFile(path, 'r') as z:
            slide_paths = sorted([p for p in z.namelist() if p.startswith('ppt/slides/slide') and p.endswith('.xml')],
                                 key=lambda p: int(Path(p).stem.replace('slide','')))
            for sp in slide_paths:
                with z.open(sp) as f:
                    try:
                        tree = ET.parse(f)
                    except ET.ParseError:
                        continue
                root = tree.getroot()
                paras = []
                for p in root.findall('.//{*}p'):
                    runs = []
                    for t in p.findall('.//{*}t'):
                        if t.text:
                            runs.append(t.text)
                    para = ''.join(runs).strip()
                    if para:
                        paras.append(para)
                if paras:
                    texts.append('\n'.join(paras))
    except Exception:
        return ''
    return '\n\n'.join(texts)

def detect_name_from_filename(filename: str) -> str:
    base = os.path.splitext(filename)[0]
    parts = base.split(' - ')
    if len(parts) >= 3:
        return parts[1].strip()
    if base.lower().startswith('a3 '):
        return base[3:].strip()
    return base

def analyze_text(text: str) -> Dict:
    low = text.lower()
    # token sets
    RDQ = [
        'research question','hypothesis','hypotheses','success criteria','decision threshold',
        'alternative explanation','method','methodology','quality control','reliability','validity'
    ]
    PILOT = [
        'pilot','implementation','what worked','what didn',"didn't work",'unexpected','refine','refinement','revised','timeline','resources','risk','backup'
    ]
    DOC = [
        'protocol','step-by-step','reproducibility','data management','metadata','ethical','privacy','consent','irb','access','security'
    ]
    COMM = [
        'figure','table','diagram','appendix','section','heading','visual','overview'
    ]
    def match(tokens):
        present = set()
        for t in tokens:
            if t in low:
                present.add(t)
        return present
    m_rdq = match(RDQ)
    m_pil = match(PILOT)
    m_doc = match(DOC)
    m_com = match(COMM)

    # headings detection
    headings = len(re.findall(r'^(#+)\s', text, flags=re.MULTILINE))
    if headings > 2:
        m_com.add('heading')

    # approach detection
    approach_tokens = {
        'simulation': ['simulation','simulate','radiance','energyplus','cfd','ladybug','honeybee'],
        'user study': ['user study','survey','interview','focus group','questionnaire'],
        'measurement': ['measurement','sensor','monitoring','environmental','observation'],
        'comparative': ['comparative','compare','alternative','alternatives'],
        'case study': ['case study','case-study']
    }
    approaches_present = []
    for name, toks in approach_tokens.items():
        if any(t in low for t in toks):
            approaches_present.append(name)

    # counts and scores
    def score(present, total):
        return len(present) / total if total else 0.0
    s_rdq = score(m_rdq, len(RDQ))
    s_pil = score(m_pil, len(PILOT))
    s_doc = score(m_doc, len(DOC))
    s_com = score(m_com, len(COMM))

    word_count = len(re.findall(r'\w+', text))
    length_factor = 1.0
    if word_count < 500:
        length_factor = 0.8
    elif word_count < 800:
        length_factor = 0.9

    est = (s_rdq*40 + s_pil*30 + s_doc*20 + s_com*10) * length_factor
    est = round(est)

    return {
        'scores': {'rdq': s_rdq, 'pilot': s_pil, 'doc': s_doc, 'comm': s_com},
        'present': {'rdq': m_rdq, 'pilot': m_pil, 'doc': m_doc, 'comm': m_com},
        'approaches': approaches_present,
        'word_count': word_count,
        'estimated_grade': est
    }

def strength_statements(data: Dict) -> List[str]:
    s = data['scores']
    present = data['present']
    approaches = data['approaches']
    out: List[Tuple[float,str]] = []
    # RDQ
    if 'hypothesis' in present['rdq'] or 'hypotheses' in present['rdq']:
        out.append((s['rdq'], 'Clear articulation of testable hypotheses'))
    if 'success criteria' in present['rdq'] or 'decision threshold' in present['rdq']:
        out.append((s['rdq'], 'Defined success criteria and decision thresholds'))
    if 'quality control' in present['rdq'] or 'reliability' in present['rdq'] or 'validity' in present['rdq']:
        out.append((s['rdq'], 'Attention to validity/reliability and quality controls'))
    if approaches:
        out.append((s['rdq'], f'Appropriate method selection ({", ".join(approaches)})'))
    # PILOT
    if 'pilot' in present['pilot'] and ('refine' in present['pilot'] or 'refinement' in present['pilot'] or 'revised' in present['pilot']):
        out.append((s['pilot'], 'Pilot learning translated into concrete refinements'))
    if 'unexpected' in present['pilot']:
        out.append((s['pilot'], 'Reflective discussion of unexpected findings'))
    # DOC
    if 'protocol' in present['doc'] or 'step-by-step' in present['doc']:
        out.append((s['doc'], 'Step-by-step protocol improves reproducibility'))
    if 'ethical' in present['doc'] or 'consent' in present['doc'] or 'privacy' in present['doc']:
        out.append((s['doc'], 'Ethical/privacy considerations are acknowledged'))
    if 'data management' in present['doc'] or 'metadata' in present['doc']:
        out.append((s['doc'], 'Data management and metadata are planned'))
    # COMM
    if s['comm'] > 0.3:
        out.append((s['comm'], 'Professional organization with clear sectioning'))
    out.sort(key=lambda x: x[0], reverse=True)
    return [msg for _, msg in out[:3]]

def improvement_statements(data: Dict) -> List[str]:
    s = data['scores']
    present = data['present']
    out: List[Tuple[float,str]] = []
    # RDQ (highest severity)
    if 'success criteria' not in present['rdq'] and 'decision threshold' not in present['rdq']:
        out.append((1.0, 'Define clear success criteria and decision thresholds'))
    if 'hypothesis' not in present['rdq'] and 'hypotheses' not in present['rdq']:
        out.append((0.95, 'State explicit, testable hypotheses aligned to the question'))
    if not ({'quality control','reliability','validity'} & present['rdq']):
        out.append((0.9, 'Add quality control procedures to support validity/reliability'))
    # PILOT
    if 'pilot' not in present['pilot']:
        out.append((0.85, 'Document a focused pilot and what it verified'))
    if not ({'refine','refinement','revised'} & present['pilot']):
        out.append((0.82, 'Translate pilot learning into specific refinements'))
    if 'unexpected' not in present['pilot']:
        out.append((0.8, 'Reflect on unexpected findings and implications'))
    # DOC
    if 'protocol' not in present['doc'] and 'step-by-step' not in present['doc']:
        out.append((0.6, 'Provide a step-by-step protocol for reproducibility'))
    if not ({'ethical','privacy','consent','irb'} & present['doc']):
        out.append((0.58, 'Address ethical/privacy and consent considerations'))
    if 'data management' not in present['doc'] and 'metadata' not in present['doc']:
        out.append((0.56, 'State a concrete data management and metadata plan'))
    # COMM (lowest severity)
    if s['comm'] < 0.3:
        out.append((0.3, 'Improve document structure with clear sections and signposting'))
    out.sort(key=lambda x: x[0], reverse=True)
    return [msg for _, msg in out[:3]]

def core_critique(data: Dict) -> str:
    # Identify weakest major category
    s = data['scores']
    order = [('Research Design', s['rdq']), ('Pilot Execution', s['pilot']), ('Method Documentation', s['doc']), ('Communication', s['comm'])]
    weakest = min(order, key=lambda x: x[1])[0]
    mapping = {
        'Research Design': 'Clarify success criteria and testable hypotheses to anchor your method.',
        'Pilot Execution': 'Make pilot learning explicit and convert it into concrete refinements.',
        'Method Documentation': 'Add a reproducible, step-by-step protocol with data and ethics plans.',
        'Communication': 'Improve structure and signposting so reasoning is easy to follow.'
    }
    return mapping[weakest]

def nice_opening(name: str) -> str:
    templates = [
        f"{name}, your submission shows thoughtful engagement with designing a workable method.",
        f"{name}, you demonstrate genuine effort translating your claim into a testable plan.",
        f"{name}, there’s clear care in how you structure your approach and learning.",
        f"{name}, your work reflects steady progress toward a robust, defensible method.",
        f"{name}, this reads as a committed attempt to build reliable evidence.",
    ]
    # rotate deterministically by name hash
    return templates[hash(name) % len(templates)]

def unique_closing(idx: int) -> str:
    closers = [
        'You’re close—tighten the essentials and A4 will benefit.',
        'Small, focused revisions now will amplify your A4 results.',
        'Carry these refinements forward and your evidence will land.',
        'Clarity plus follow-through will make your analysis credible.',
        'Lean into the method—reliability beats breadth every time.',
        'Finish the basics strong and A4 becomes straightforward.',
        'Keep the structure firm and the story will carry itself.',
        'Sharpen criteria and the next decisions become obvious.',
        'Anchor with protocol—consistency will do the heavy lifting.',
        'Tighten the chain of reasoning and you’ll be persuasive.'
    ]
    return closers[idx % len(closers)]

def main():
    files = sorted([p for p in A3_DIR.iterdir() if p.is_file() and p.suffix.lower() in {'.pdf','.docx','.pptx','.txt'}])
    sections = []
    for idx, f in enumerate(files, start=1):
        name = detect_name_from_filename(f.name)
        # get text
        if f.suffix.lower() == '.pdf':
            text = read_text_from_pdf(f)
        elif f.suffix.lower() == '.docx':
            text = read_text_from_docx(f)
        elif f.suffix.lower() == '.pptx':
            text = read_text_from_pptx(f)
        else:
            text = read_text_from_txt(f)
        analysis = analyze_text(text)
        strengths = strength_statements(analysis)
        improvements = improvement_statements(analysis)
        critique = core_critique(analysis)
        grade = analysis['estimated_grade']

        # Build section
        anchor = re.sub(r'[^a-z0-9]+','-', name.lower()).strip('-')
        sec = []
        sec.append(f"## {idx}. {name} {{#{anchor}}}")
        sec.append('\n### Opening Recognition')
        sec.append(nice_opening(name))
        sec.append('\n### Core Critique')
        sec.append(critique)
        sec.append('\n### Strengths (Top 3)')
        if strengths:
            for s in strengths:
                sec.append(f"- {s}")
        else:
            sec.append("- Evidence of progress toward a coherent method")
        sec.append('\n### Areas to Improve (Top 3)')
        if improvements:
            for s in improvements:
                sec.append(f"- {s}")
        else:
            sec.append("- Clarify the most critical elements of the method")
        sec.append('\n### Closing')
        sec.append(unique_closing(idx-1))
        sec.append(f"\n**Estimated Grade: {grade}/100**")
        sec.append('\n---\n')
        sections.append('\n'.join(sec))

    header = '''---
title: "A3 Assessment: Test Plan + Pilot Study"
subtitle: "Automated first-pass feedback aligned to rubric"
format:
  html:
    toc: true
    toc-depth: 2
    number-sections: true
---

# Assessment Notes

This document provides a structured first-pass assessment generated from each submission’s text, aligned to the Assignment 3 rubric (Research Design 40%, Pilot 30%, Documentation 20%, Communication 10%). It should be reviewed by the instructor for final grading.

---

# Individual Feedback
'''
    OUT_QMD.write_text(header + '\n'.join(sections), encoding='utf-8')
    print(f"Wrote {OUT_QMD}")

if __name__ == '__main__':
    main()

