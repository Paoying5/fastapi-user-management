from typing import Annotated, Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    StringConstraints,
    field_validator,
)

from app.schemas.post import PostSimple


UserRole = Literal[
    "user",
    "admin",
]

UserName = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=2,
        max_length=100,
    ),
]

FullName = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        max_length=100,
    ),
]


class StrictRequestModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )


class UserCreate(StrictRequestModel):
    name: UserName

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=128,
    )

    full_name: FullName | None = None


class UserUpdate(StrictRequestModel):
    name: UserName

    email: EmailStr

    role: UserRole

    full_name: FullName | None = None


class UserPatch(StrictRequestModel):
    name: UserName | None = None

    email: EmailStr | None = None

    role: UserRole | None = None

    full_name: FullName | None = None

    @field_validator(
        "name",
        "email",
        "role",
    )
    @classmethod
    def non_nullable_fields_cannot_be_null(
        cls,
        value,
    ):
        if value is None:
            raise ValueError(
                "Field cannot be null"
            )

        return value


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole
    full_name: str | None = None

    posts: list[PostSimple] = Field(
        default_factory=list,
    )

    model_config = ConfigDict(
        from_attributes=True,
    )