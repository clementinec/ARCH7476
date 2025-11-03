#!/usr/bin/env python3
"""
Extract text from PDF files in the A3 directory for assessment purposes.
"""

import os
import PyPDF2
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using PyPDF2"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            
            # Extract text from all pages
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
            
            return text
    except Exception as e:
        return f"Error extracting text from {pdf_path}: {str(e)}"

def process_a3_submissions():
    """Process all PDF files in the A3 directory"""
    
    # Define paths
    a3_dir = Path("/Users/guo/tprojs/ARCH7476/A3")
    output_dir = Path("/Users/guo/tprojs/ARCH7476/A3/extracted_text")
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    # Find all PDF files in A3 directory
    pdf_files = list(a3_dir.glob("*.pdf"))
    
    print(f"Found {len(pdf_files)} PDF files to process")
    
    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        
        # Extract text
        extracted_text = extract_text_from_pdf(pdf_file)
        
        # Create output filename
        output_filename = pdf_file.stem + "_extracted.txt"
        output_path = output_dir / output_filename
        
        # Save extracted text
        try:
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(f"=== EXTRACTED TEXT FROM: {pdf_file.name} ===\n\n")
                output_file.write(extracted_text)
            
            print(f"✓ Saved: {output_filename}")
            
        except Exception as e:
            print(f"✗ Error saving {output_filename}: {str(e)}")
    
    print(f"\nText extraction complete. Files saved to: {output_dir}")
    return output_dir

if __name__ == "__main__":
    output_directory = process_a3_submissions()
    print(f"\nNext step: Check the extracted text files in {output_directory}")