from typing import Annotated

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
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


class StrictRequestModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )


class PostCreate(StrictRequestModel):
    title: PostTitle

    content: str | None = None


class PostUpdate(StrictRequestModel):
    title: PostTitle

    content: str | None = None


class PostPatch(StrictRequestModel):
    title: PostTitle | None = None

    content: str | None = None

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
    owner: UserSimple

    model_config = ConfigDict(
        from_attributes=True,
    )