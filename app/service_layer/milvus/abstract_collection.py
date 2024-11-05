"""Abstract collection."""

from abc import ABC, abstractmethod

from svc.domain.models.entity import Entity


class AbstractCollection(ABC):
    """Abstract collection."""

    def __init__(self) -> None:
        super().__init__()

    def add(self, entity: Entity) -> None:
        """Adds aggregate to the store."""
        self._add(entity)

    @abstractmethod
    def _add(self, entity: Entity) -> None:
        """Implement by adding the entity to the store."""
