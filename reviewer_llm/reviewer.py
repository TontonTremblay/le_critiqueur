import os
from typing import Dict, List, Optional
from dotenv import load_dotenv
from openai import OpenAI
from .pdf_processor import PDFProcessor
from .prompts import (
    CLAIMS_PROMPT,
    EXPERIMENTS_PROMPT,
    RELATED_WORK_PROMPT,
    REPRODUCIBILITY_PROMPT,
    ETHICS_PROMPT
)

class PaperReviewer:
    def __init__(self, model: str = "gpt-4-turbo-preview"):
        """Initialize the paper reviewer with OpenAI client."""
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.pdf_processor = PDFProcessor()

    def review_paper(self, pdf_path: str) -> Dict:
        """Main method to review a paper comprehensively."""
        print("  - Starting PDF text extraction...")
        # Extract text from PDF
        paper_text = self.pdf_processor.extract_text(pdf_path)
        print("  - PDF text extraction completed")
        
        # Perform all review aspects
        print("  - Starting claims analysis...")
        claims = self.analyze_claims(paper_text)
        print("  - Claims analysis completed")
        
        print("  - Starting experimental design review...")
        experiments = self.review_experiments(paper_text)
        print("  - Experimental design review completed")
        
        print("  - Starting related work analysis...")
        related_work = self.analyze_related_work(paper_text)
        print("  - Related work analysis completed")
        
        print("  - Starting reproducibility assessment...")
        reproducibility = self.check_reproducibility(paper_text)
        print("  - Reproducibility assessment completed")
        
        print("  - Starting ethics review...")
        ethics = self.review_ethics(paper_text)
        print("  - Ethics review completed")
        
        review = {
            "claims": claims,
            "experiments": experiments,
            "related_work": related_work,
            "reproducibility": reproducibility,
            "ethics": ethics
        }
        
        return review

    def analyze_claims(self, paper_text: str) -> Dict:
        """Analyze paper claims and evidence."""
        print("    - Sending claims analysis request to OpenAI...")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": CLAIMS_PROMPT},
                {"role": "user", "content": paper_text}
            ]
        )
        print("    - Received claims analysis response")
        return self._parse_response(response.choices[0].message.content)

    def review_experiments(self, paper_text: str) -> Dict:
        """Review experimental design."""
        print("    - Sending experimental design review request to OpenAI...")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": EXPERIMENTS_PROMPT},
                {"role": "user", "content": paper_text}
            ]
        )
        print("    - Received experimental design review response")
        return self._parse_response(response.choices[0].message.content)

    def analyze_related_work(self, paper_text: str) -> Dict:
        """Analyze related work section."""
        print("    - Sending related work analysis request to OpenAI...")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": RELATED_WORK_PROMPT},
                {"role": "user", "content": paper_text}
            ]
        )
        print("    - Received related work analysis response")
        return self._parse_response(response.choices[0].message.content)

    def check_reproducibility(self, paper_text: str) -> Dict:
        """Check reproducibility aspects."""
        print("    - Sending reproducibility assessment request to OpenAI...")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": REPRODUCIBILITY_PROMPT},
                {"role": "user", "content": paper_text}
            ]
        )
        print("    - Received reproducibility assessment response")
        return self._parse_response(response.choices[0].message.content)

    def review_ethics(self, paper_text: str) -> Dict:
        """Review ethics and impact statements."""
        print("    - Sending ethics review request to OpenAI...")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": ETHICS_PROMPT},
                {"role": "user", "content": paper_text}
            ]
        )
        print("    - Received ethics review response")
        return self._parse_response(response.choices[0].message.content)

    def _parse_response(self, response: str) -> Dict:
        """Parse the LLM response into a structured format."""
        # This is a simple implementation - you might want to make it more robust
        # based on your specific needs
        try:
            # Assuming the response is in a structured format
            # You might want to use a more sophisticated parsing method
            return {"raw_response": response}
        except Exception as e:
            return {"error": str(e), "raw_response": response} 