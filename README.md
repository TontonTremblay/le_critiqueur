# LLM Paper Reviewer

An AI-powered paper review system that provides comprehensive academic paper reviews using OpenAI's GPT models.

## Features

- Deep analysis of academic papers in PDF format
- Structured review based on multiple aspects:
  - Claims analysis and evidence evaluation
  - Experimental design critique
  - Related work analysis
  - Reproducibility assessment
  - Ethics and impact evaluation
- Configurable review criteria based on venue requirements
- Detailed feedback with specific recommendations

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

```python
from reviewer_llm import PaperReviewer

reviewer = PaperReviewer()
review = reviewer.review_paper("path/to/paper.pdf")
print(review)
```

## API Documentation

### PaperReviewer Class

The main class for paper review functionality.

#### Methods

- `review_paper(pdf_path: str) -> Dict`: Main method to review a paper
  - Input: Path to PDF file
  - Output: Dictionary containing structured review results

- `analyze_claims(pdf_path: str) -> Dict`: Analyze paper claims and evidence
- `review_experiments(pdf_path: str) -> Dict`: Review experimental design
- `analyze_related_work(pdf_path: str) -> Dict`: Analyze related work section
- `check_reproducibility(pdf_path: str) -> Dict`: Check reproducibility aspects
- `review_ethics(pdf_path: str) -> Dict`: Review ethics and impact statements

## Project Structure

```
reviewer_llm/
├── README.md
├── requirements.txt
├── .env
├── reviewer_llm/
│   ├── __init__.py
│   ├── reviewer.py
│   ├── pdf_processor.py
│   ├── prompts/
│   │   ├── claims.py
│   │   ├── experiments.py
│   │   ├── related_work.py
│   │   ├── reproducibility.py
│   │   └── ethics.py
│   └── utils/
│       ├── __init__.py
│       └── text_processing.py
└── tests/
    └── test_reviewer.py
```

## License

MIT License 