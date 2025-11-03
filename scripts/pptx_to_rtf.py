#!/usr/bin/env python3
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

def rtf_escape(s: str) -> str:
    out = []
    for ch in s:
        code = ord(ch)
        if ch in ['\\', '{', '}']:
            out.append('\\' + ch)
        elif 0x20 <= code <= 0x7E:
            out.append(ch)
        else:
            out.append(f"\\u{code}?")
    return ''.join(out)

def extract_text_from_pptx(pptx_path: Path):
    texts_by_slide = []
    with zipfile.ZipFile(pptx_path, 'r') as z:
        # Collect slide files in order
        slide_paths = sorted([p for p in z.namelist() if p.startswith('ppt/slides/slide') and p.endswith('.xml')],
                             key=lambda p: int(Path(p).stem.replace('slide','')))
        for sp in slide_paths:
            with z.open(sp) as f:
                try:
                    tree = ET.parse(f)
                except ET.ParseError:
                    texts_by_slide.append([])
                    continue
            root = tree.getroot()
            # find all paragraph nodes and join their text runs
            # match any namespace: {namespace}t for text runs, {ns}p for paragraphs
            paragraphs = []
            for p in root.findall('.//{*}p'):
                runs = []
                for t in p.findall('.//{*}t'):
                    if t.text:
                        runs.append(t.text)
                para = ''.join(runs).strip()
                if para:
                    paragraphs.append(para)
            texts_by_slide.append(paragraphs)
    return texts_by_slide

def write_rtf(slides, out_path: Path):
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('{\\rtf1\\ansi\\deff0{\\fonttbl{\\f0 Arial;}}\n')
        f.write('\\fs22 ')
        for idx, paras in enumerate(slides, start=1):
            f.write('\\b ' + rtf_escape(f'Slide {idx}') + ' \\b0\\par\n')
            if not paras:
                f.write(rtf_escape(' (no visible text)') + '\\par\n')
                continue
            for para in paras:
                line = rtf_escape(' - ' + para)
                f.write(line + '\\par\n')
            f.write('\\par\n')
        f.write('}\n')

def main():
    if len(sys.argv) != 3:
        print('Usage: pptx_to_rtf.py input.pptx output.rtf', file=sys.stderr)
        sys.exit(2)
    inp = Path(sys.argv[1])
    out = Path(sys.argv[2])
    slides = extract_text_from_pptx(inp)
    out.parent.mkdir(parents=True, exist_ok=True)
    write_rtf(slides, out)

if __name__ == '__main__':
    main()

