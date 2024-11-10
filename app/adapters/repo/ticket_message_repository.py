"""Ticket message repository."""

from app.adapters.repo import SqlAlchemyRepository
from app.service_layer.repositories import TicketMessageRepository

from app.domain import models


class SqlAlchemyTicketMessageRepository(SqlAlchemyRepository, TicketMessageRepository):
    """Sqlalchemy ticket message repository."""

    model_type = models.TicketMessage
