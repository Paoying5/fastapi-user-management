from fastapi import APIRouter, Depends, Query, status

from app.dependencies import get_current_user, get_post_service
from app.models import User
from app.schemas import MessageResponse, PostCreate, PostPatch, PostResponse, PostUpdate
from app.services.post_service import PostService


router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(
    post_data: PostCreate,
    service: PostService = Depends(get_post_service),
    current_user: User = Depends(get_current_user),
):
    return service.create_post(post_data, current_user.id)


@router.get("/", response_model=list[PostResponse])
def get_posts(
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    search: str = Query(default="", max_length=100),
    service: PostService = Depends(get_post_service),
):
    return service.get_posts(limit, offset, search)


@router.get("/me", response_model=list[PostResponse])
def get_my_posts(
    service: PostService = Depends(get_post_service),
    current_user: User = Depends(get_current_user),
):
    return service.get_my_posts(current_user.id)


@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, service: PostService = Depends(get_post_service)):
    post = service.get_post(post_id)
    if post is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post


@router.put("/{post_id}", response_model=PostResponse)
def update_post(
    post_id: int,
    post_data: PostUpdate,
    service: PostService = Depends(get_post_service),
    current_user: User = Depends(get_current_user),
):
    return service.update_post(post_id, post_data, current_user.id)


@router.patch("/{post_id}", response_model=PostResponse)
def patch_post(
    post_id: int,
    post_data: PostPatch,
    service: PostService = Depends(get_post_service),
    current_user: User = Depends(get_current_user),
):
    return service.patch_post(post_id, post_data, current_user.id)


@router.delete("/{post_id}", response_model=MessageResponse)
def delete_post(
    post_id: int,
    service: PostService = Depends(get_post_service),
    current_user: User = Depends(get_current_user),
):
    service.delete_post(post_id, current_user.id)
    return MessageResponse(message="Post deleted successfully")
