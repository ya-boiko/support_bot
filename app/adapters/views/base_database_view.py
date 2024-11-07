"""Base database view."""


class BaseDatabaseView:
    """Base database list view."""

    def __init__(self, session_factory) -> None:
        self._session_factory = session_factory
