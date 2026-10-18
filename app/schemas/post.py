from datetime import datetime
from typing import Annotated, Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    StringConstraints,
    field_validator,
)


PostTitle = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=2,
        max_length=255,
    ),
]


PostStatus = Literal[
    "draft",
    "published",
    "archived",
]


class StrictRequestModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )


class PostCreate(StrictRequestModel):
    title: PostTitle
    content: str | None = None
    status: PostStatus = "published"


class PostUpdate(StrictRequestModel):
    title: PostTitle
    content: str | None = None


class PostPatch(StrictRequestModel):
    title: PostTitle | None = None
    content: str | None = None
    status: PostStatus | None = None

    @field_validator("title")
    @classmethod
    def title_cannot_be_null(
        cls,
        value,
    ):
        if value is None:
            raise ValueError(
                "title cannot be null"
            )

        return value

    @field_validator("status")
    @classmethod
    def status_cannot_be_null(
        cls,
        value,
    ):
        if value is None:
            raise ValueError(
                "status cannot be null"
            )

        return value


class PostSimple(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class UserSimple(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class PostResponse(BaseModel):
    id: int
    title: str
    content: str | None
    user_id: int

    status: PostStatus
    created_at: datetime
    updated_at: datetime

    owner: UserSimple

    model_config = ConfigDict(
        from_attributes=True,
    )