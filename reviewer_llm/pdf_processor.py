from typing import Optional
from PyPDF2 import PdfReader

class PDFProcessor:
    def __init__(self):
        """Initialize the PDF processor."""
        pass

    def extract_text(self, pdf_path: str) -> str:
        """
        Extract text from a PDF file.
        
        Args:
            pdf_path (str): Path to the PDF file
            
        Returns:
            str: Extracted text from the PDF
            
        Raises:
            FileNotFoundError: If the PDF file doesn't exist
            ValueError: If the PDF file is corrupted or empty
        """
        try:
            print(f"      - Opening PDF file: {pdf_path}")
            reader = PdfReader(pdf_path)
            
            # Check if PDF is empty
            if len(reader.pages) == 0:
                raise ValueError("PDF file is empty")
            
            print(f"      - PDF has {len(reader.pages)} pages")
            
            # Extract text from all pages
            text = ""
            for i, page in enumerate(reader.pages, 1):
                print(f"      - Processing page {i}/{len(reader.pages)}")
                text += page.extract_text() + "\n"
            
            # Remove excessive whitespace
            text = " ".join(text.split())
            
            if not text.strip():
                raise ValueError("No text could be extracted from the PDF")
            
            print(f"      - Successfully extracted {len(text)} characters")
            return text
            
        except FileNotFoundError:
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        except Exception as e:
            raise ValueError(f"Error processing PDF: {str(e)}")

    def get_page_count(self, pdf_path: str) -> int:
        """
        Get the number of pages in a PDF file.
        
        Args:
            pdf_path (str): Path to the PDF file
            
        Returns:
            int: Number of pages in the PDF
        """
        reader = PdfReader(pdf_path)
        return len(reader.pages) 