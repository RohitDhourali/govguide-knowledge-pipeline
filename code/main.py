from preprocessing import *

INPUT_FILE = "data/raw/company_registration.txt"

OUTPUT_FILE = "output/company_registration_clean.txt"


text = load_text(INPUT_FILE)

cleaned_text = clean_text(text)

save_text(cleaned_text, OUTPUT_FILE)

print("Cleaning completed successfully.")