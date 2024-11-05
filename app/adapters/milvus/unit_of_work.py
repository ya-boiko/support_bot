"""Unit of work."""

from app.service_layer.milvus import MilvusUnitOfWork
from app.service_layer.milvus import UnitOfWork as IUnitOfWork
from app.service_layer.milvus.collections import SupportChatsCollection

from .collections import MilvusSupportChatsCollection


class UnitOfWork(MilvusUnitOfWork, IUnitOfWork):
    """UoW."""

    support_chats: SupportChatsCollection = None

    def __init__(self, client) -> None:
        super().__init__(client)

    def _init_repositories(self) -> list[object]:
        self.support_chats = MilvusSupportChatsCollection(self.client)

        return [
            self.support_chats,
        ]
