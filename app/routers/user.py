from fastapi import (
    APIRouter,
    Depends,
    Query,
    status,
)

from app.dependencies import (
    get_admin_user,
    get_user_service,
)
from app.models.user import User
from app.schemas import (
    APIResponse,
    UserCreate,
    UserPatch,
    UserResponse,
    UserUpdate,
)
from app.services.user_service import UserService
from app.utils.response import response


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/",
    response_model=APIResponse,
    summary="Get all users",
)
def get_users(
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Số lượng bản ghi tối đa trả về",
    ),
    offset: int = Query(
        default=0,
        ge=0,
        description="Số lượng bản ghi bỏ qua",
    ),
    search: str = Query(
        default="",
        max_length=100,
        description="Tìm kiếm theo tên hoặc email",
    ),
    service: UserService = Depends(
        get_user_service
    ),
    _admin: User = Depends(
        get_admin_user
    ),
):
    users = service.get_users(
        limit=limit,
        offset=offset,
        search=search,
    )

    data = [
        UserResponse.model_validate(
            user
        ).model_dump()
        for user in users
    ]

    return response(
        "Users retrieved successfully",
        data,
    )


@router.get(
    "/{user_id}",
    response_model=APIResponse,
    summary="Get user by ID",
)
def get_user(
    user_id: int,
    service: UserService = Depends(
        get_user_service
    ),
    _admin: User = Depends(
        get_admin_user
    ),
):
    user = service.get_user(
        user_id
    )

    data = (
        UserResponse
        .model_validate(user)
        .model_dump()
    )

    return response(
        "User found",
        data,
    )


@router.post(
    "/",
    response_model=APIResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create user",
)
def create_user(
    user: UserCreate,
    service: UserService = Depends(
        get_user_service
    ),
):
    db_user = service.create_user(
        user
    )

    data = (
        UserResponse
        .model_validate(db_user)
        .model_dump()
    )

    return response(
        "User created successfully",
        data,
    )


@router.put(
    "/{user_id}",
    response_model=APIResponse,
    summary="Replace user",
)
def update_user(
    user_id: int,
    user: UserUpdate,
    service: UserService = Depends(
        get_user_service
    ),
    _admin: User = Depends(
        get_admin_user
    ),
):
    updated_user = service.update_user(
        user_id,
        user,
    )

    data = (
        UserResponse
        .model_validate(updated_user)
        .model_dump()
    )

    return response(
        "User updated successfully",
        data,
    )


@router.patch(
    "/{user_id}",
    response_model=APIResponse,
    summary="Partially update user",
)
def patch_user(
    user_id: int,
    user_data: UserPatch,
    service: UserService = Depends(
        get_user_service
    ),
    _admin: User = Depends(
        get_admin_user
    ),
):
    updated_user = service.patch_user(
        user_id,
        user_data,
    )

    data = (
        UserResponse
        .model_validate(updated_user)
        .model_dump()
    )

    return response(
        "User partially updated successfully",
        data,
    )


@router.delete(
    "/{user_id}",
    response_model=APIResponse,
    summary="Delete user",
)
def delete_user(
    user_id: int,
    service: UserService = Depends(
        get_user_service
    ),
    _admin: User = Depends(
        get_admin_user
    ),
):
    service.delete_user(
        user_id
    )

    return response(
        "User deleted successfully",
        None,
    )