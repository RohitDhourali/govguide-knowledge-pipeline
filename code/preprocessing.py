import re
import unicodedata


def load_text(file_path):
    """
    Load text from a UTF-8 encoded file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def normalize_unicode(text):
    """
    Normalize Unicode characters.
    Prevents different Unicode representations
    of the same Nepali characters.
    """

    return unicodedata.normalize("NFC", text)


def normalize_line_endings(text):
    """
    Convert all line endings into '\n'.
    """

    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    return text


def normalize_spaces(text):
    """
    Replace multiple spaces or tabs with a single space.
    """

    return re.sub(r"[ \t]+", " ", text)


def normalize_blank_lines(text):
    """
    Keep at most one blank line between paragraphs.
    """

    return re.sub(r"\n{3,}", "\n\n", text)


def clean_text(text):
    """
    Run the complete preprocessing pipeline.
    """

    text = normalize_unicode(text)

    text = normalize_line_endings(text)

    text = normalize_spaces(text)

    text = normalize_blank_lines(text)

    return text.strip()


def save_text(text, output_path):
    """
    Save cleaned text.
    """

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)