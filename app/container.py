"""Dependency injections."""

from dependency_injector import containers, providers
from pymilvus import MilvusClient

from app.adapters.milvus.unit_of_work import UnitOfWork as MilvusUnitOfWork
from app.service_layer.handlers import mapping
from svc.service_layer.message_bus import MessageBus


class Container(containers.DeclarativeContainer):
    """Dependency injection container."""

    wiring_config = containers.WiringConfiguration(
        packages=['app'],
    )
    config = providers.Configuration()

    # milvus

    milvus_client = providers.Singleton(MilvusClient, config.milvus.url)

    # uow

    milvus_uow = providers.Factory(MilvusUnitOfWork, milvus_client)

    # bus

    event_handlers = providers.Object(mapping.EVENT_HANDLERS)
    command_handlers = providers.Object(mapping.COMMAND_HANDLERS)
    bus = providers.Singleton(MessageBus, milvus_uow, event_handlers, command_handlers)
