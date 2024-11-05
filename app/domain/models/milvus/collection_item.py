"""Collection item and collection item's text."""

from dataclasses import dataclass

from svc.domain.models.entity import Entity


@dataclass
class CollectionItemText(Entity):
    question: str
    answer: str


@dataclass
class CollectionItem(Entity):
    vector: list[float]
    text: CollectionItemText
    subject: str

    @classmethod
    def create(cls, vector: list[float], text: CollectionItemText, subject: str):
        return CollectionItem(
            vector=vector,
            text=text,
            subject=subject,
        )

    def as_dict(self):
        return {
            'vector': self.vector,
            'text': vars(self.text),
            'subject': self.subject,
        }
