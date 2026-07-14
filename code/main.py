from preprocessing import *



INPUT_FILE = "extracted_text/Chapter_0.txt"

OUTPUT_FILE = "output/Chapter_0_clean.txt"


text = load_text(INPUT_FILE)

cleaned_text = clean_text(text)

save_text(cleaned_text, OUTPUT_FILE)

print("Cleaning completed successfully.")