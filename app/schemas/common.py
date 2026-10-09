from typing import Generic, Literal, TypeVar

from pydantic import BaseModel


T = TypeVar("T")


class APIResponse(
    BaseModel,
    Generic[T],
):
    status: Literal["success"] = "success"
    message: str
    data: T | None = None


class MessageResponse(BaseModel):
    message: str