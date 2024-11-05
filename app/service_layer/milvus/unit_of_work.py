"""Milvus Unit of work."""

from pymilvus import MilvusClient

from svc.service_layer.unit_of_work import AbstractUnitOfWork

from .collections import SupportChatsCollection


class MilvusUnitOfWork(AbstractUnitOfWork):
    """UoW implementation for Milvus."""

    _repos: list
    client: MilvusClient

    def __init__(self, client) -> None:
        self.client = client

    def __enter__(self):
        self._repos = self._init_repositories()
        return super().__enter__()

    def commit(self):
        pass

    def rollback(self):
        pass

    def _init_repositories(self) -> list[object]:  # pylint: disable=unused-argument
        """
        Override this method to initialize repositories on entering the context.

        Return the repositories that need to be analyzed for `seen` entities after the event
        is handled.
        """
        return []


class UnitOfWork(AbstractUnitOfWork):
    """UoW."""

    support_chats: SupportChatsCollection = None
