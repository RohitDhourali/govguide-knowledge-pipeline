import json

from reader import load_text

from generator import generate_objects


INPUT = "output/company_registration_clean.txt"

OUTPUT = "output/company_registration_objects.json"


text = load_text(INPUT)

objects = generate_objects(

    text,

    "company_registration.pdf"

)

with open(

    OUTPUT,

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        [obj.to_dict() for obj in objects],

        f,

        ensure_ascii=False,

        indent=4

    )


print("Knowledge Objects Generated Successfully.")