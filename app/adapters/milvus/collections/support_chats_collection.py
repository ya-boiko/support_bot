"""Milvus support chats collection."""

from app.service_layer.milvus.collections import SupportChatsCollection

from .base_collection import BaseMilvusCollection


class MilvusSupportChatsCollection(BaseMilvusCollection, SupportChatsCollection):
    """Milvus support chats collection."""

    name: str = 'support_chats'
