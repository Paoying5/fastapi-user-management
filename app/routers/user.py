from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
import crud
from app.crud import user_crud as crud
from app.dependencies import get_db
from app.schemas import (
    APIResponse,
    UserCreate,
    UserPatch,
    UserResponse,
    UserUpdate,
    user,
)
from app.utils.response import response


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# GET /users
@router.get(
    "/",
    response_model=APIResponse,
    summary="Get all users",
    description="""
Retrieve all users stored in the database.
""",
)
def get_users(

    db: Session = Depends(get_db)

):

    repo = UserRepository(db)
    users = repo.get_all()

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
    response_model=APIResponse,
    summary="Get user by ID",
    description="""
Retrieve one user.

Return 404 if user does not exist.
""",
    responses={
        404: {
            "description": "User not found"
        }
    }
)
def get_user(

    user_id:int,

    db: Session = Depends(get_db)

):

    repo = UserRepository(db)

    user = repo.get_by_id(user_id)
    
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
    response_model=APIResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create user",
    description="""
Create a new user.
""",
    responses={
        409: {
            "description": "Email already exists"
        }
    }
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
    response_model=APIResponse,
    summary="Replace user",
    description="""
Replace entire user.
""",
    responses={
        404:{
            "description":"User not found"
        },
        409:{
            "description":"Email already exists"
        }
    }
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
    summary="Partially update user",
    description="""
Update selected fields.
""",
    responses={
        404:{
            "description":"User not found"
        },
        409:{
            "description":"Email already exists"
        }
    }
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
@router.delete(
    "/{user_id}",
    response_model=APIResponse,
    summary="Delete user",
    description="""
Delete one user.
""",
    responses={
        404:{
            "description":"User not found"
        }
    }
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    repo = UserRepository(db)

    user = repo.get_by_id(user_id)

    if not user:
        raise HTTPException(
                status_code=404,
                detail="User not found"
    )

    repo.delete(user)

    return response(
    "User deleted successfully",
    None
)