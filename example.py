from reviewer_llm import PaperReviewer

def main():
    # Initialize the reviewer
    reviewer = PaperReviewer()
    
    # Path to your PDF paper
    pdf_path = "path/to/your/paper.pdf"
    
    try:
        # Get a comprehensive review
        review = reviewer.review_paper(pdf_path)
        
        # Print the review sections
        print("\n=== Claims Analysis ===")
        print(review["claims"])
        
        print("\n=== Experimental Design Review ===")
        print(review["experiments"])
        
        print("\n=== Related Work Analysis ===")
        print(review["related_work"])
        
        print("\n=== Reproducibility Assessment ===")
        print(review["reproducibility"])
        
        print("\n=== Ethics and Impact Review ===")
        print(review["ethics"])
        
    except Exception as e:
        print(f"Error reviewing paper: {str(e)}")

if __name__ == "__main__":
    main() 