"""Ticket message."""

import uuid
from dataclasses import dataclass
from typing import Optional, TypeAlias
from datetime import datetime, UTC

from .entity import Entity


Vector: TypeAlias = list[float]


@dataclass
class TicketMessage(Entity):
    """Ticket message model."""

    id: uuid.UUID

    message_vector: Vector
    message: str
    response: str

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @classmethod
    def create(cls, message_vector: Vector, message: str, response: str, **kwargs) -> 'TicketMessage':
        """Creates the class object."""
        return TicketMessage(
            id=kwargs.get('id', uuid.uuid4()),
            message_vector=message_vector,
            message=message,
            response=response,
            created_at=kwargs.get('created_at', datetime.now(UTC)),
            updated_at=kwargs.get('updated_at', datetime.now(UTC)),
        )

    def update(self, changes: dict):
        """Updates the attributes."""
        for (field, value) in changes.items():
            setattr(self, field, value)

        return self

    def as_dict(self) -> dict:
        """Returns a dict representation of the object."""
        return {
            'id': self.id,
            'message_vector': self.message_vector,
            'message': self.message,
            'response': self.response,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
