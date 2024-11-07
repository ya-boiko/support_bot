"""Ticket message."""

import uuid
from dataclasses import dataclass
from typing import Optional, TypeAlias
from datetime import datetime

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
