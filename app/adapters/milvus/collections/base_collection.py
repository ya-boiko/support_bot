"""Base Milvus collection."""

import abc

from pymilvus import MilvusClient

from app.domain.models.milvus import CollectionItem
from app.service_layer.milvus import AbstractCollection


class BaseMilvusCollection(AbstractCollection, abc.ABC):
    """Base Milvus collection."""

    client: MilvusClient
    base_dimension: int         # Dimension of vector embedding
    name: str

    def __init__(self, client: MilvusClient, **kwargs):
        super().__init__()
        self.client = client
        self.base_dimension = kwargs.get('base_dimension', 1536)

    def is_collection_exists(self):
        return self.client.has_collection(collection_name=self.name)

    def drop_collection(self):
        if self.client.has_collection(collection_name=self.name):
            self.client.drop_collection(collection_name=self.name)

    def create_collection(self):
        self.client.create_collection(collection_name=self.name, dimension=self.base_dimension, auto_id=True)

    def _add(self, entity: list[CollectionItem]) -> dict:
        return self.client.insert(collection_name=self.name, data=[d.as_dict() for d in entity])

    def search(self, data: list[float]):
        return self.client.search(
            collection_name=self.name,  # target collection
            data=data,  # query vectors
            limit=2,  # number of returned entities
            output_fields=['text', 'subject'],  # specifies fields to be returned
        )
