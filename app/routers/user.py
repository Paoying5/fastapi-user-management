from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import user as user_crud
from app.dependencies import get_db
from app.schemas import (
    APIResponse,
    UserCreate,
    UserPatch,
    UserResponse,
    UserUpdate,
)
from app.utils.response import response

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# GET /users
@router.get(
    "/",
    response_model=APIResponse
)
def get_users(

    db: Session = Depends(get_db)

):

    users = user_crud.get_users(db)

    data = [

        UserResponse
        .model_validate(user)
        .model_dump()

        for user in users

    ]

    return response(

        "Users retrieved successfully",

        data

    )

# GET User by ID
@router.get(
    "/{user_id}",
    response_model=APIResponse
)
def get_user(

    user_id:int,

    db: Session = Depends(get_db)

):

    user = crud.get_user(db, user_id)
    if not user:

        raise HTTPException(

            status_code=404,

            detail="User not found"

        )

    return response(

        "User found",

        UserResponse
        .model_validate(user)
        .model_dump()

    )

# Create User
@router.post(
    "/",
    response_model=APIResponse
)
def create_user(

    user:UserCreate,

    db:Session=Depends(get_db)

):

    db_user=crud.create_user(

        db,

        user

    )

    return response(

        "User created successfully",

        UserResponse
        .model_validate(db_user)
        .model_dump()

    )

# Update user
@router.put(
    "/{user_id}",
    response_model=APIResponse
)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):

    updated_user = crud.update_user(
        db,
        user_id,
        user
    )

    if not updated_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return response(
        "User updated successfully",
        UserResponse
        .model_validate(updated_user)
        .model_dump()
    )

@router.patch(
    "/{user_id}",
    response_model=APIResponse,
)
def patch_user(
    user_id: int,
    user_data: UserPatch,
    db: Session = Depends(get_db),
):
    updated_user = user_crud.patch_user(
        db,
        user_id,
        user_data,
    )

    if updated_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return response(
        "User partially updated successfully",
        UserResponse
        .model_validate(updated_user)
        .model_dump(),
    )

# Delete user
@router.delete("/{user_id}", response_model=APIResponse)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_user(db, user_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return response(
        "User deleted successfully",
        None
    )