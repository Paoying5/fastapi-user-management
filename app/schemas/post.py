from pydantic import BaseModel, ConfigDict, Field


class PostCreate(BaseModel):
    title: str = Field(
        min_length=2,
        max_length=255,
    )

    content: str | None = None


class PostUpdate(BaseModel):
    title: str = Field(
        min_length=2,
        max_length=255,
    )

    content: str | None = None


class PostPatch(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=2,
        max_length=255,
    )

    content: str | None = None


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