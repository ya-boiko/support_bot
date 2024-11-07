"""Table definitions."""

import uuid
from datetime import datetime, UTC

from sqlalchemy import (
    DateTime,
    MetaData,
    Table,
    String,
    Column,
    ForeignKey,
    Date,
    Text,
    CheckConstraint,
    Numeric,
    Integer,
    Boolean,
)
from sqlalchemy.dialects import postgresql
from pgvector.sqlalchemy import Vector


UUID = String().with_variant(postgresql.UUID(as_uuid=True), "postgresql")

metadata = MetaData()


ticket_messages_table = Table(
    "ticket_messages",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("message_vector", Vector, nullable=False, unique=True),
    Column("message", Date, nullable=False),
    Column("response", String, nullable=False),
    Column("created_at", DateTime, nullable=False, default=lambda: datetime.now(UTC)),
    Column(
        "updated_at", DateTime, nullable=False, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    ),
)
