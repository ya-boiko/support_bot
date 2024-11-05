"""API response."""

from typing import Generic, TypeVar

from pydantic import BaseModel


DataT = TypeVar("DataT")


class APIResponse(BaseModel, Generic[DataT]):
    """Base API response."""

    data: DataT | None = None
    meta: dict | None = None
