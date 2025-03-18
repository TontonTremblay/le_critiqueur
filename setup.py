from setuptools import setup, find_packages

setup(
    name="reviewer_llm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=0.19.0",
        "PyPDF2>=3.0.0",
        "pydantic>=2.0.0",
        "numpy>=1.21.0",
        "pytest>=7.0.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="An AI-powered paper review system using OpenAI's GPT models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/reviewer_llm",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 