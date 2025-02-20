"""Repositories."""

from abc import ABC, abstractmethod

from app.domain.models import Entity


class AbstractRepository(ABC):
    """Abstract repository."""

    def get(self, entity_id):
        """Returns the aggregate by ID."""
        return self._get(entity_id)

    @abstractmethod
    def delete(self, entity: Entity) -> None:
        """Deletes aggregate from the store."""

    @abstractmethod
    def _add(self, entity: Entity) -> None:
        """Implement by adding the entity to the store."""

    @abstractmethod
    def _get(self, entity_id) -> Entity:
        """Implement by returning the entity"""

    def add(self, entity: Entity) -> None:
        """Adds aggregate to the store."""
        self._add(entity)
