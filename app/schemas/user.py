from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.schemas.post import PostSimple


class UserCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
    )

    email: EmailStr

    role: str = Field(
        default="user",
        min_length=2,
        max_length=30,
    )

    password: str = Field(
        min_length=6,
        max_length=128,
    )

    full_name: str | None = None


class UserUpdate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
    )

    email: EmailStr

    role: str = Field(
        min_length=2,
        max_length=30,
    )

    full_name: str | None = Field(
    default=None,
    max_length=100,
)


class UserPatch(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    email: EmailStr | None = None

    role: str | None = Field(
        default=None,
        min_length=2,
        max_length=30,
    )

    full_name: str | None = Field(
    default=None,
    max_length=100,
)


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    full_name: str | None = None

    posts: list[PostSimple] = Field(
        default_factory=list,
    )

    model_config = ConfigDict(
        from_attributes=True,
    )