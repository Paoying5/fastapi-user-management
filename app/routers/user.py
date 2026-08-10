from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_user_service
from app.schemas import APIResponse, UserCreate, UserPatch, UserResponse, UserUpdate
from app.services.user_service import UserService
from app.utils.response import response


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=APIResponse, summary="Get all users")
def get_users(service: UserService = Depends(get_user_service)):
    users = service.get_users()
    data = [UserResponse.model_validate(user).model_dump() for user in users]
    return response("Users retrieved successfully", data)


@router.get("/{user_id}", response_model=APIResponse, summary="Get user by ID")
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return response("User found", UserResponse.model_validate(user).model_dump())


@router.post("/", response_model=APIResponse, status_code=status.HTTP_201_CREATED, summary="Create user")
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    db_user = service.create_user(user)
    return response("User created successfully", UserResponse.model_validate(db_user).model_dump())


@router.put("/{user_id}", response_model=APIResponse, summary="Replace user")
def update_user(
    user_id: int,
    user: UserUpdate,
    service: UserService = Depends(get_user_service),
):
    updated_user = service.update_user(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return response("User updated successfully", UserResponse.model_validate(updated_user).model_dump())


@router.patch("/{user_id}", response_model=APIResponse, summary="Partially update user")
def patch_user(
    user_id: int,
    user_data: UserPatch,
    service: UserService = Depends(get_user_service),
):
    updated_user = service.patch_user(user_id, user_data)
    if updated_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return response("User partially updated successfully", UserResponse.model_validate(updated_user).model_dump())


@router.delete("/{user_id}", response_model=APIResponse, summary="Delete user")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return response("User deleted successfully", None)
