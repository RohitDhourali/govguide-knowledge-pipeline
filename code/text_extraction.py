import os
import fitz  # PyMuPDF


# -----------------------------
# Configuration
# -----------------------------

INPUT_FOLDER = "data/raw"
OUTPUT_FOLDER = "extracted_text"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# -----------------------------
# PDF Text Extraction
# -----------------------------

def extract_pdf_text(pdf_path):
    """
    Extract all text from a PDF using PyMuPDF.
    """

    document = fitz.open(pdf_path)

    full_text = []

    for page_number, page in enumerate(document):

        text = page.get_text("text")

        full_text.append(text)

    document.close()

    return "\n".join(full_text)


# -----------------------------
# Save Extracted Text
# -----------------------------

def save_text(text, output_path):

    with open(output_path, "w", encoding="utf-8") as file:

        file.write(text)


# -----------------------------
# Process All PDFs
# -----------------------------

def process_all_pdfs():

    for filename in os.listdir(INPUT_FOLDER):

        if filename.lower().endswith(".pdf"):

            pdf_path = os.path.join(INPUT_FOLDER, filename)

            print(f"Processing: {filename}")

            extracted_text = extract_pdf_text(pdf_path)

            txt_filename = os.path.splitext(filename)[0] + ".txt"

            output_path = os.path.join(OUTPUT_FOLDER, txt_filename)

            save_text(extracted_text, output_path)

            print(f"Saved: {txt_filename}")

    print("\nAll PDFs processed successfully.")


# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":

    process_all_pdfs()