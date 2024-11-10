"""ORM."""

from sqlalchemy.orm import registry

from app.adapters.orm import tables, instrumentation
from app.domain import models


mapper_registry = registry()
metadata = tables.metadata

instrumentation.instrument_entity()


def bind_mappers():
    """Binds ORM mappers."""

    mapper_registry.map_imperatively(models.TicketMessage, tables.ticket_messages_table)
