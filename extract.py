import os
import re
import fitz  # PyMuPDF

def extract_emails_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text += page.get_text()

        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        return emails
    except Exception as e:
        print(f"Error extracting emails from {pdf_path}: {e}")
        return []

def search_emails_in_directory(directory):
    emails_found = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                emails_in_file = extract_emails_from_pdf(file_path)
                if emails_in_file:
                    emails_found.extend(emails_in_file)

    return emails_found

if __name__ == "__main__":
    # Replace 'your_directory_path' with the path to the root directory containing your PDF files
    directory_path = 'your_directory_path'
    
    extracted_emails = search_emails_in_directory(directory_path)

    if extracted_emails:
        print("Email addresses found:")
        for email in extracted_emails:
            print(email)
    else:
        print("No email addresses found in the specified directory.")
