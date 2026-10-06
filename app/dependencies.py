from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database import get_db
from app.models import User
from app.services.auth_service import AuthService
from app.services.post_service import PostService
from app.services.user_service import UserService


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
)


def get_user_service(
    db: Session = Depends(get_db),
) -> UserService:
    return UserService(db)


def get_post_service(
    db: Session = Depends(get_db),
) -> PostService:
    return PostService(db)


def get_auth_service(
    db: Session = Depends(get_db),
) -> AuthService:
    return AuthService(db)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    service: AuthService = Depends(get_auth_service),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={
            "WWW-Authenticate": "Bearer",
        },
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        subject = payload.get("sub")

        if not isinstance(subject, str) or not subject:
            raise credentials_exception

    except JWTError as exc:
        raise credentials_exception from exc

    # New token format:
    # sub = string representation of user.id
    if subject.isdigit():
        user = service.get_user_by_id(
            int(subject)
        )

    # Backward compatibility:
    # old tokens used email as the JWT subject.
    else:
        user = service.get_user_by_email(
            subject
        )

    if user is None:
        raise credentials_exception

    return user


def get_admin_user(
    current_user: User = Depends(get_current_user),
) -> User:
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )

    return current_user