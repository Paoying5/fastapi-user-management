from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)
from sqlalchemy.orm import Session

from app.crud import post as post_crud
from app.dependencies import get_current_user, get_db
from app.models import User
from app.schemas import (
    MessageResponse,
    PostCreate,
    PostPatch,
    PostResponse,
    PostUpdate,
)


router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


@router.post(
    "/",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_post(
    post_data: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return post_crud.create_post(
        db,
        post_data,
        current_user.id,
    )


@router.get(
    "/",
    response_model=list[PostResponse],
)
def get_posts(
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
    ),
    offset: int = Query(
        default=0,
        ge=0,
    ),
    search: str = Query(
        default="",
        max_length=100,
    ),
    db: Session = Depends(get_db),
):
    return post_crud.get_posts(
        db,
        limit,
        offset,
        search,
    )


# Route tĩnh phải nằm trước /{post_id}.
@router.get(
    "/me",
    response_model=list[PostResponse],
)
def get_my_posts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return post_crud.get_my_posts(
        db,
        current_user.id,
    )


@router.get(
    "/{post_id}",
    response_model=PostResponse,
)
def get_post(
    post_id: int,
    db: Session = Depends(get_db),
):
    post = post_crud.get_post(
        db,
        post_id,
    )

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    return post


@router.put(
    "/{post_id}",
    response_model=PostResponse,
)
def update_post(
    post_id: int,
    post_data: PostUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = post_crud.update_post(
        db,
        post_id,
        post_data,
        current_user.id,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    if result is False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not own this post",
        )

    return result


@router.patch(
    "/{post_id}",
    response_model=PostResponse,
)
def patch_post(
    post_id: int,
    post_data: PostPatch,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = post_crud.patch_post(
        db,
        post_id,
        post_data,
        current_user.id,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    if result is False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not own this post",
        )

    return result


@router.delete(
    "/{post_id}",
    response_model=MessageResponse,
)
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = post_crud.delete_post(
        db,
        post_id,
        current_user.id,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    if result is False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not own this post",
        )

    return MessageResponse(
        message="Post deleted successfully",
    )