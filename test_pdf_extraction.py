# test_pdf_extraction.py
from utils import extract_text_from_pdf

# Specify the path to your PDF document
pdf_path = r"C:\Users\bodak\OneDrive\Desktop\AI Assignment\OmniValueSolutions\scrum_master_en.pdf"

# Extract text from the PDF using the utility function
text_content = extract_text_from_pdf(pdf_path)

# Print the extracted text
print(text_content)
