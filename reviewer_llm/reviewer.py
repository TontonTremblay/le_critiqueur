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
        # Extract text from PDF
        paper_text = self.pdf_processor.extract_text(pdf_path)
        
        # Perform all review aspects
        review = {
            "claims": self.analyze_claims(paper_text),
            "experiments": self.review_experiments(paper_text),
            "related_work": self.analyze_related_work(paper_text),
            "reproducibility": self.check_reproducibility(paper_text),
            "ethics": self.review_ethics(paper_text)
        }
        
        return review

    def analyze_claims(self, paper_text: str) -> Dict:
        """Analyze paper claims and evidence."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": CLAIMS_PROMPT},
                {"role": "user", "content": paper_text}
            ]
        )
        return self._parse_response(response.choices[0].message.content)

    def review_experiments(self, paper_text: str) -> Dict:
        """Review experimental design."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": EXPERIMENTS_PROMPT},
                {"role": "user", "content": paper_text}
            ]
        )
        return self._parse_response(response.choices[0].message.content)

    def analyze_related_work(self, paper_text: str) -> Dict:
        """Analyze related work section."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": RELATED_WORK_PROMPT},
                {"role": "user", "content": paper_text}
            ]
        )
        return self._parse_response(response.choices[0].message.content)

    def check_reproducibility(self, paper_text: str) -> Dict:
        """Check reproducibility aspects."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": REPRODUCIBILITY_PROMPT},
                {"role": "user", "content": paper_text}
            ]
        )
        return self._parse_response(response.choices[0].message.content)

    def review_ethics(self, paper_text: str) -> Dict:
        """Review ethics and impact statements."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": ETHICS_PROMPT},
                {"role": "user", "content": paper_text}
            ]
        )
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