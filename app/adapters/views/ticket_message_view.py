"""View for the ticket message."""

import uuid

from app.domain.models import TicketMessage

from .base_database_view import BaseDatabaseView


class TicketMessageView(BaseDatabaseView):
    """Ticket message view."""

    def __call__(self, ticket_message_id: uuid.UUID) -> TicketMessage:
        """Returns the ticket message by ID."""
        with (self._session_factory() as session):
            scope = session.query(
                TicketMessage
            ).filter(
                TicketMessage.id == ticket_message_id
            )

            result = scope.first()

            return result
