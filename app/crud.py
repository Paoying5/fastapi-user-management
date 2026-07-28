from app import schemas
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from sqlalchemy import desc
from sqlalchemy import or_
from sqlalchemy import and_
from app.models import User, Post
from app.core.security import hash_password, verify_password


# =====================================================
# USER
# =====================================================

def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def get_user_by_email(
    db: Session,
    email: str
):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def create_user(
    db: Session,
    user
):
    db_user = User(
        name=user.name,
        email=user.email,
        role=user.role,
        password=hash_password(user.password)
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user


def update_user(
    db: Session,
    user_id: int,
    user
):
    db_user = get_user(
        db,
        user_id
    )

    if not db_user:
        return None

    db_user.name = user.name
    db_user.email = user.email
    db_user.role = user.role

    db.commit()

    db.refresh(db_user)

    return db_user


def delete_user(
    db: Session,
    user_id: int
):
    db_user = get_user(
        db,
        user_id
    )

    if not db_user:
        return False

    db.delete(db_user)

    db.commit()

    return True


# =====================================================
# AUTH
# =====================================================

def login_user(
    db: Session,
    email: str,
    password: str
):

    user = get_user_by_email(
        db,
        email
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.password
    ):
        return None

    return user


# =====================================================
# POST
# =====================================================

def create_post(
    db: Session,
    post,
    user_id: int
):
    db_post = Post(
        title=post.title,
        content=post.content,
        user_id=user_id
    )

    db.add(db_post)

    db.commit()

    db.refresh(db_post)

    return db_post


def get_posts(
    db: Session,
    limit: int ,
    offset: int,
    search: str,
    user_id: int | None = None
):
    query = (
        db.query(Post)
        .options(
            joinedload(Post.owner)
        )
    )

    if user_id:

        query = query.filter(

            and_(

                Post.title.ilike(f"%{search}%"),

                Post.user_id == user_id

            )

        )

    else:

        query = query.filter(

            Post.title.ilike(f"%{search}%")

        )

    return (

        query

        .order_by(desc(Post.id))

        .offset(offset)

        .limit(limit)

        .all()

    )


def get_post(
    db: Session,
    post_id: int
):
    return (
        db.query(Post)
        .options(
            joinedload(Post.owner)
        )
        .filter(
            Post.id == post_id
        )
        .first()
    )


def get_my_posts(
    db: Session,
    user_id: int
):
    return (
        db.query(Post)
        .options(
            joinedload(Post.owner)
        )
        .filter(
            Post.user_id == user_id
        )
        .order_by(
            desc(Post.id)
        )
        .all()
    )

def get_posts_by_ids(
    db: Session,
    ids: list[int]
):
    return (
        db.query(Post)
        .options(
            joinedload(Post.owner)
        )
        .filter(
            Post.id.in_(ids)
        )
        .order_by(
            desc(Post.id)
        )
        .all()
    )

def get_posts_between(
    db: Session,
    start: int,
    end: int
):
    return (
        db.query(Post)
        .options(
            joinedload(Post.owner)
        )
        .filter(
            Post.id.between(start, end)
        )
        .order_by(
            desc(Post.id)
        )
        .all()
    )

def count_posts(
    db: Session
):
    return (
        db.query(Post)
        .count()
    )

def count_users(
    db: Session
):
    return (
        db.query(User)
        .count()
    )

def count_admins(
    db: Session
):
    return (
        db.query(User)
        .filter(User.role == "admin")
        .count()
    )

# =====================================================
# UPDATE POST
# =====================================================
def update_post(
    db: Session,
    post_id: int,
    post: schemas.PostCreate,
    user_id: int
):
    db_post = get_post(
        db,
        post_id
    )

    if not db_post:
        return None

    if db_post.user_id != user_id:
        return False

    db_post.title = post.title
    db_post.content = post.content

    db.commit()

    db.refresh(db_post)

    return db_post


# =====================================================
# DELETE POST
# =====================================================

def delete_post(
    db: Session,
    post_id: int,
    user_id: int
):
    db_post = get_post(
        db,
        post_id
    )

    if not db_post:
        return None

    if db_post.user_id != user_id:
        return False

    db.delete(db_post)

    db.commit()

    return True