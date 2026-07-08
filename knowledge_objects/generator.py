from detector import heading_type
from models import KnowledgeObject


def generate_objects(text, source_file):

    lines = text.splitlines()

    objects = []

    counter = 1

    current_main = None
    current_sub = None
    current_title = None
    current_content = []


    def save_object():

        nonlocal counter

        if current_title is None:
            return

        obj = KnowledgeObject(

            id=f"BR-KO-{counter:03}",

            domain="Business Registration",

            document="company_registration",

            section=current_title,

            content="\n".join(current_content).strip(),

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

        if h == "main":

            save_object()

            current_main = line
            current_sub = None
            current_title = line
            current_content = []

        elif h == "sub":

            save_object()

            current_sub = line
            current_title = f"{current_main} > {current_sub}"

            current_content = []

        elif h == "alpha":

            save_object()

            if current_sub:

                current_title = f"{current_main} > {current_sub} > {line}"

            else:

                current_title = f"{current_main} > {line}"

            current_content = []

        else:

            current_content.append(line)

    save_object()

    return objects