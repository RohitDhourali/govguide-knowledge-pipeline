import os
from pathlib import Path

import fitz
import pytesseract
from PIL import Image, ImageFilter, ImageOps


class PdfExtractor:

    def __init__(
        self,
        input_folder="input_pdfs",
        output_folder="extracted_text",
        tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    ):

        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(exist_ok=True)

        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def extract_all_pdfs(self):
        """OCR every PDF in the input folder."""

        pdf_files = list(self.input_folder.glob("*.pdf"))

        if not pdf_files:
            print("No PDF files found.")
            return

        for pdf_path in pdf_files:
            self.extract_pdf(pdf_path)

    def extract_pdf(self, pdf_path):
        """Extract one PDF and save it as a text file."""

        print(f"Processing: {pdf_path.name}")

        doc = fitz.open(pdf_path)

        all_text = []

        for page_number in range(len(doc)):
            page = doc.load_page(page_number)

            print(f"  OCR Page {page_number + 1}/{len(doc)}")

            text = self._ocr_page(page)

            all_text.append(f"\n===== Page {page_number + 1} =====\n")
            all_text.append(text)

        doc.close()

        output_file = self.output_folder / f"{pdf_path.stem}.txt"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("".join(all_text))

        print(f"Saved -> {output_file}")

    def _preprocess_for_ocr(self, img):

        gray = img.convert("L")

        gray = ImageOps.autocontrast(gray, cutoff=1)

        gray = gray.filter(ImageFilter.SHARPEN)

        histogram = gray.histogram()

        total_pixels = sum(histogram)

        weight_bg = 0
        sum_bg = 0
        max_variance = 0
        threshold = 128

        total_intensity = sum(i * histogram[i] for i in range(256))

        for t in range(256):

            weight_bg += histogram[t]

            if weight_bg == 0:
                continue

            weight_fg = total_pixels - weight_bg

            if weight_fg == 0:
                break

            sum_bg += t * histogram[t]

            mean_bg = sum_bg / weight_bg
            mean_fg = (total_intensity - sum_bg) / weight_fg

            variance = weight_bg * weight_fg * (mean_bg - mean_fg) ** 2

            if variance > max_variance:
                max_variance = variance
                threshold = t

        binary = gray.point(
            lambda x: 255 if x > threshold else 0,
            "1"
        )

        binary = binary.filter(ImageFilter.MedianFilter(size=3))

        return binary

    def _ocr_page(self, page):

        pix = page.get_pixmap(dpi=300)

        img = Image.frombytes(
            "RGB",
            [pix.width, pix.height],
            pix.samples
        )

        processed = self._preprocess_for_ocr(img)

        text = pytesseract.image_to_string(
            processed,
            lang="nep",
            config="--psm 4 --oem 1",
        )

        return text
extractor = PdfExtractor()
extractor.extract_all_pdfs()