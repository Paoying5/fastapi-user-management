from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
)

from app.schemas.post import PostSimple


UserRole = Literal[
    "user",
    "admin",
]


class UserCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
    )

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=128,
    )

    # Client không được tự chọn role khi đăng ký.
    # Service luôn tạo user mới với role="user".
    full_name: str | None = Field(
        default=None,
        max_length=100,
    )


class UserUpdate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
    )

    email: EmailStr

    role: UserRole

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

    role: UserRole | None = None

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