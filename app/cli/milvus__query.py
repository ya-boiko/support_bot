import os
from pprint import pprint

from openai import OpenAI
from pymilvus import MilvusClient
from dotenv import load_dotenv
from dependency_injector.wiring import Provide, inject

from app.container import Container
from app.service_layer.milvus import MilvusUnitOfWork
from app.settings import Settings


@inject
def query(
    data,
    uow: MilvusUnitOfWork = Provide[Container.milvus_uow],
):
    with uow:
        return uow.support_chats.search(  data=data)


if __name__ == '__main__':
    container = Container()
    container.wire(modules=[__name__])
    settings = Settings()

    container.config.from_dict(settings.model_dump())

    openai_client = OpenAI(api_key=settings.openai.api_secret_key)

    # queries = ['I have trouble accessing my course.']
    queries = ['Which course should I choose?.']

    query_vectors = [
        vec.embedding
        for vec in openai_client.embeddings.create(input=queries, model=settings.openai.embedding_model).data
    ]

    res = query(query_vectors)

    for q in queries:
        print("Query:", q)
        for result in res:
            pprint(result)
        print("\n")