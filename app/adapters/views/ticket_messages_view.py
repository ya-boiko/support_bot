"""View for the ticket messages."""

import uuid

from app.domain.models import TicketMessage

from .base_database_view import BaseDatabaseView


class TicketMessagesView(BaseDatabaseView):
    """Ticket messages view."""

    def __call__(self) -> TicketMessage:
        """Returns the list of ticket messages."""
        with (self._session_factory() as session):
            scope = session.query(
                TicketMessage
            ).order_by(
                TicketMessage.created_at
            )

            result = scope.all()

            return result
