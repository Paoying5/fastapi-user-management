from sqlalchemy import CheckConstraint, Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    __table_args__ = (
        CheckConstraint(
            "role IN ('user', 'admin')",
            name="ck_users_role_allowed",
        ),
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    name = Column(
        String(100),
        nullable=False,
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    role = Column(
        String(50),
        nullable=False,
        default="user",
        server_default="user",
    )

    password = Column(
        String(255),
        nullable=False,
    )

    full_name = Column(
        String(100),
        nullable=True,
    )

    posts = relationship(
        "Post",
        back_populates="owner",
        cascade="all, delete-orphan",
    )