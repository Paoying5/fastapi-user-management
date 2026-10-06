from typing import NoReturn

from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserPatch, UserUpdate


class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository(db)

    def get_users(
        self,
        limit: int = 10,
        offset: int = 0,
        search: str = "",
    ) -> list[User]:
        return self.repository.get_all(
            limit=limit,
            offset=offset,
            search=search,
        )

    def get_user(
        self,
        user_id: int,
    ) -> User | None:
        return self.repository.get_by_id(
            user_id
        )

    def create_user(
        self,
        user_data: UserCreate,
    ) -> User:
        email = self._normalize_email(
            str(user_data.email)
        )

        # Friendly early check.
        # This is useful, but it is NOT the final protection
        # against concurrent requests.
        if (
            self.repository.get_by_email(email)
            is not None
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists",
            )

        user = User(
            name=user_data.name,
            email=email,
            role="user",
            password=hash_password(
                user_data.password
            ),
            full_name=user_data.full_name,
        )

        try:
            user = self.repository.add(user)

            self.db.commit()
            self.db.refresh(user)

            return user

        except IntegrityError as exc:
            self._handle_integrity_error(exc)

        except Exception:
            self.db.rollback()
            raise

    def update_user(
        self,
        user_id: int,
        user_data: UserUpdate,
    ) -> User | None:
        user = self.repository.get_by_id(
            user_id
        )

        if user is None:
            return None

        email = self._normalize_email(
            str(user_data.email)
        )

        if (
            user.email != email
            and self.repository.get_by_email(email)
            is not None
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists",
            )

        user.name = user_data.name
        user.email = email
        user.role = user_data.role
        user.full_name = user_data.full_name

        return self._commit_update(user)

    def patch_user(
        self,
        user_id: int,
        user_data: UserPatch,
    ) -> User | None:
        user = self.repository.get_by_id(
            user_id
        )

        if user is None:
            return None

        update_data = user_data.model_dump(
            exclude_unset=True
        )

        if (
            "email" in update_data
            and update_data["email"] is not None
        ):
            email = self._normalize_email(
                str(update_data["email"])
            )

            if (
                user.email != email
                and self.repository.get_by_email(
                    email
                )
                is not None
            ):
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Email already exists",
                )

            update_data["email"] = email

        for field_name, value in update_data.items():
            setattr(
                user,
                field_name,
                value,
            )

        return self._commit_update(user)

    def delete_user(
        self,
        user_id: int,
    ) -> bool:
        user = self.repository.get_by_id(
            user_id
        )

        if user is None:
            return False

        try:
            self.repository.delete(user)
            self.db.commit()

            return True

        except Exception:
            self.db.rollback()
            raise

    def _commit_update(
        self,
        user: User,
    ) -> User:
        try:
            user = self.repository.update(user)

            self.db.commit()
            self.db.refresh(user)

            return user

        except IntegrityError as exc:
            self._handle_integrity_error(exc)

        except Exception:
            self.db.rollback()
            raise

    @staticmethod
    def _normalize_email(
        email: str,
    ) -> str:
        return email.strip().lower()

    def _handle_integrity_error(
        self,
        exc: IntegrityError,
    ) -> NoReturn:
        self.db.rollback()

        original_error = str(
            exc.orig
        ).lower()

        diagnostic = getattr(
            exc.orig,
            "diag",
            None,
        )

        constraint_name = getattr(
            diagnostic,
            "constraint_name",
            None,
        )

        email_constraints = {
            "ix_users_email",
            "users_email_key",
        }

        is_email_conflict = (
            constraint_name
            in email_constraints
            or (
                "users.email"
                in original_error
                and (
                    "unique"
                    in original_error
                    or "duplicate"
                    in original_error
                )
            )
        )

        if is_email_conflict:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists",
            ) from exc

        raise exc