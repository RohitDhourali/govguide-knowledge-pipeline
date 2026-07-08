import json
import re
from pathlib import Path

# -----------------------------
# Configuration
# -----------------------------

INPUT_FILE = Path("output/company_registration_objects.json")
OUTPUT_FILE = Path("output/company_registration_chunks.json")

# Approximate number of words per chunk.
# (Later you can replace this with true token counting.)
MAX_WORDS = 250

# Number of words to overlap between chunks
OVERLAP_WORDS = 30


# -----------------------------
# Utilities
# -----------------------------

def word_count(text):
    return len(text.split())


def split_into_units(text):
    """
    Split a knowledge object into logical units.

    Priority:
    1. New lines
    2. Paragraphs
    3. Sentences
    """

    text = text.strip()

    # Split by newline first
    units = [u.strip() for u in text.split("\n") if u.strip()]

    if len(units) > 1:
        return units

    # If there are no newlines, split into sentences.
    units = re.split(r'(?<=[।!?])\s+', text)

    return [u.strip() for u in units if u.strip()]


def build_chunks(units):
    """
    Group logical units into chunks without breaking units.
    """

    chunks = []

    current = []
    current_words = 0

    for unit in units:

        wc = word_count(unit)

        if current_words + wc <= MAX_WORDS:

            current.append(unit)
            current_words += wc

        else:

            chunks.append("\n".join(current))

            # overlap
            overlap = []

            words = " ".join(current).split()

            if OVERLAP_WORDS > 0:

                overlap_text = " ".join(words[-OVERLAP_WORDS:])

                overlap.append(overlap_text)

            current = overlap + [unit]
            current_words = word_count(" ".join(current))

    if current:
        chunks.append("\n".join(current))

    return chunks


# -----------------------------
# Main
# -----------------------------

def chunk_knowledge_objects(objects):

    all_chunks = []

    for obj in objects:

        units = split_into_units(obj["content"])

        chunks = build_chunks(units)

        for idx, chunk in enumerate(chunks, start=1):

            chunk_obj = {

                "chunk_id": f"{obj['id']}-C{idx}",

                "parent_knowledge_object_id": obj["id"],

                "chunk_index": idx,

                "domain": obj["domain"],

                "document": obj["document"],

                "section": obj["section"],

                "source": obj["source"],

                "keywords": obj.get("keywords", []),

                "content": chunk

            }

            all_chunks.append(chunk_obj)

    return all_chunks


def main():

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        objects = json.load(f)

    chunks = chunk_knowledge_objects(objects)

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=4)

    print(f"Knowledge Objects : {len(objects)}")
    print(f"Generated Chunks  : {len(chunks)}")
    print(f"Saved to          : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()