"""Ticket message's commands."""

import uuid
from dataclasses import dataclass

from .command import Command


@dataclass
class CreateTicketMessage(Command):
    """Command for creating a ticket message."""

    message: str
    response: str


@dataclass
class UpdateTicketMessage(Command):
    """Command for updating a ticket message."""

    id: uuid.UUID
    message: str
    response: str


@dataclass
class DeleteTicketMessage(Command):
    """Command for deleting a ticket message."""

    id: uuid.UUID
