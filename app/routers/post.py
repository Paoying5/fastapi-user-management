from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.database import get_db
from app.routers.auth import get_current_user
from app import crud
from app import schemas

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.post("/")
def create_post(

    post: schemas.PostCreate,

    db: Session = Depends(get_db),

    current_user = Depends(get_current_user)

):

    return crud.create_post(

        db,

        post,

        current_user.id

    )

@router.get(
    "/",
    response_model=list[schemas.PostResponse]
)
def get_posts(

    limit: int = 10,

    offset: int = 0,

    db: Session = Depends(get_db)

):

    return crud.get_posts(

        db,

        limit,

        offset

    )


@router.get(
    "/me",
    response_model=list[schemas.PostResponse]
)
def my_posts(

    db: Session = Depends(get_db),

    current_user = Depends(get_current_user)

):

    return crud.get_my_posts(

        db,

        current_user.id

    )

@router.get(
    "/{post_id}",
    response_model=schemas.PostResponse
)
def get_post(
    post_id: int,
    db: Session = Depends(get_db)
):

    post = crud.get_post(
        db,
        post_id
    )

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    return post
