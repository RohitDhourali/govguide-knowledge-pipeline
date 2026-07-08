from detector import heading_type
from models import KnowledgeObject


def generate_objects(text, source_file):

    lines = text.splitlines()

    objects = []

    counter = 1

    # Current document hierarchy
    current_chapter = None
    current_part = None
    current_main = None
    current_sub = None
    current_subsub = None
    current_alpha = None
    current_clause = None

    current_content = []

    def build_title():
        """Build hierarchical title from active headings."""

        parts = []

        if current_chapter:
            parts.append(current_chapter)

        if current_part:
            parts.append(current_part)

        if current_main:
            parts.append(current_main)

        if current_sub:
            parts.append(current_sub)

        if current_subsub:
            parts.append(current_subsub)

        if current_alpha:
            parts.append(current_alpha)

        if current_clause:
            parts.append(current_clause)

        return " > ".join(parts)

    def save_object():

        nonlocal counter

        title = build_title()

        if not title:
            return

        content = "\n".join(current_content).strip()

        # Don't save empty objects
        if not content:
            return

        obj = KnowledgeObject(
            id=f"BR-KO-{counter:03}",
            domain="Business Registration",
            document="company_registration",
            section=title,
            content=content,
            source=source_file,
            keywords=[]
        )

        objects.append(obj)

        counter += 1

    for raw in lines:

        line = raw.strip()

        if not line:
            continue

        h = heading_type(line)

        if h == "chapter":

            save_object()

            current_chapter = line
            current_part = None
            current_main = None
            current_sub = None
            current_subsub = None
            current_alpha = None
            current_clause = None
            current_content = []

        elif h == "part":

            save_object()

            current_part = line
            current_main = None
            current_sub = None
            current_subsub = None
            current_alpha = None
            current_clause = None
            current_content = []

        elif h == "main":

            save_object()

            current_main = line
            current_sub = None
            current_subsub = None
            current_alpha = None
            current_clause = None
            current_content = []

        elif h == "sub":

            save_object()

            current_sub = line
            current_subsub = None
            current_alpha = None
            current_clause = None
            current_content = []

        elif h == "subsub":

            save_object()

            current_subsub = line
            current_alpha = None
            current_clause = None
            current_content = []

        elif h == "alpha":

            save_object()

            current_alpha = line
            current_clause = None
            current_content = []

        elif h == "clause":

            save_object()

            current_clause = line
            current_content = []

        else:

            current_content.append(line)

    save_object()
    

    return objects