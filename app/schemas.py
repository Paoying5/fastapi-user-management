from typing import Optional
from typing import Any

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import ConfigDict

# UserCreate
class UserCreate(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr

    role: str = Field(
        min_length=2,
        max_length=30
    )

    password: str = Field(
        min_length=6
    )

class PostSimple(BaseModel):

    id: int

    title: str

    model_config = ConfigDict(
        from_attributes=True
    )

# UserResponse
class UserResponse(BaseModel):

    id: int

    name: str

    email: EmailStr

    role: str

    posts: list[PostSimple] = []

    model_config = ConfigDict(
        from_attributes=True
    )

# UserUpdate
class UserUpdate(BaseModel):

    name: str

    email: EmailStr

    role: str

    model_config = ConfigDict(from_attributes=True)

# UserPatch
class UserPatch(BaseModel):

    name: Optional[str] = None

    email: Optional[EmailStr] = None

    role: Optional[str] = None

# LoginRequest
class LoginRequest(BaseModel):

    email: EmailStr

    password: str

# TokenResponse
class TokenResponse(BaseModel):

    access_token: str

    token_type: str

# APIResponse
class APIResponse(BaseModel):

    status: str

    message: str

    data: Any | None = None

# Token Schema
class Token(BaseModel):
    
    access_token: str

    token_type: str

# Schema dùng để tạo bài viết (Request Body)
class PostCreate(BaseModel):

    title: str

    content: str


# Usersimple
class UserSimple(BaseModel):

    id: int

    name: str

    email: EmailStr

    model_config = ConfigDict(
        from_attributes=True
    )



# Schema trả về thông tin bài viết (Response Body)
class PostResponse(BaseModel):

    id: int

    title: str

    content: str

    owner: UserSimple

    model_config = ConfigDict(
        from_attributes=True
    )
