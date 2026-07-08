import json


class KnowledgeObject:
    """
    Represents one logical section of a document.
    """

    def __init__(self, object_id, title, content):
        self.object_id = object_id
        self.title = title
        self.content = content

    def to_dict(self):
        return {
            "id": self.object_id,
            "title": self.title,
            "content": self.content
        }
    def save_objects(objects, output_file):
     """
    Save knowledge objects as JSON.
    """

    data = [obj.to_dict() for obj in objects]

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )