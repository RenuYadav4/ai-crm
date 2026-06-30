from datetime import datetime

from sqlalchemy import (Boolean, DateTime, ForeignKey, String,)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from core.database import Base

class User(Base):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.id")
    )

    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id")
    )

    organization = relationship(
        "Organization",
        back_populates="users"
    )

    role = relationship(
        "Role",
        back_populates="users"
    )

    refresh_tokens = relationship(
        "RefreshToken",
        back_populates="user",
        cascade="all, delete"
    )
