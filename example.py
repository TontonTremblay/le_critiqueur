from reviewer_llm import PaperReviewer
import os
from dotenv import load_dotenv
from datetime import datetime

def save_review_to_markdown(review: dict, pdf_path: str, output_dir: str = "reviews"):
    """Save the review results to a markdown file."""
    # Create reviews directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename from PDF name and timestamp
    pdf_name = os.path.basename(pdf_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{os.path.splitext(pdf_name)[0]}_{timestamp}.md"
    output_path = os.path.join(output_dir, filename)
    
    print(f"\nSaving review to: {output_path}")
    
    with open(output_path, "w", encoding="utf-8") as f:
        # Write header
        f.write(f"# Paper Review: {pdf_name}\n\n")
        f.write(f"*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
        
        # Write each section
        sections = {
            "claims": "## Claims Analysis",
            "experiments": "## Experimental Design Review",
            "related_work": "## Related Work Analysis",
            "reproducibility": "## Reproducibility Assessment",
            "ethics": "## Ethics and Impact Review"
        }
        
        for key, title in sections.items():
            f.write(f"\n{title}\n\n")
            content = review[key].get("raw_response", "No content available")
            f.write(content + "\n")
    
    print(f"✅ Review saved successfully to {output_path}")

def main():
    print("\n=== Starting Paper Review Process ===\n")
    
    # Check if .env file exists and load it
    if not os.path.exists('.env'):
        print("❌ Error: .env file not found!")
        print("Please copy .env.example to .env and add your OpenAI API key")
        return
    
    print("✅ .env file found")
    load_dotenv()
    
    # Check if API key is set
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in .env file!")
        print("Please add your OpenAI API key to the .env file")
        return
    print("✅ OpenAI API key found")
    
    # Initialize the reviewer
    print("\nInitializing PaperReviewer...")
    reviewer = PaperReviewer()
    print("✅ PaperReviewer initialized successfully")
    
    # Path to your PDF paper
    pdf_path = "/Users/jtremblay/Downloads/2411.16537v1.pdf"
    print(f"\nAttempting to review paper at: {pdf_path}")
    
    try:
        # Get a comprehensive review
        print("\nStarting comprehensive review...")
        review = reviewer.review_paper(pdf_path)
        print("✅ Review completed successfully")
        
        # Save review to markdown file
        save_review_to_markdown(review, pdf_path)
        
        # Print summary to console
        print("\n=== Review Summary ===")
        for section in ["claims", "experiments", "related_work", "reproducibility", "ethics"]:
            print(f"\n{section.upper()}:")
            content = review[section].get("raw_response", "No content available")
            # Print first 200 characters as preview
            print(content[:200] + "..." if len(content) > 200 else content)
        
    except FileNotFoundError as e:
        print(f"\n❌ Error: PDF file not found: {str(e)}")
        print("Please provide a valid path to your PDF file")
    except Exception as e:
        print(f"\n❌ Error during review process: {str(e)}")
        print("Please check the error message above for details")

if __name__ == "__main__":
    main() 