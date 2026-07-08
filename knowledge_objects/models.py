from dataclasses import dataclass, asdict


@dataclass
class KnowledgeObject:

    id: str

    domain: str

    document: str

    section: str

    content: str

    source: str

    keywords: list

    def to_dict(self):
        return asdict(self)