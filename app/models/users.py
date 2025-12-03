from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.roles import RoleModel
    from app.models.feedbacks import FeedbacksModel


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(300), nullable=False)
    image_url: Mapped[str] = mapped_column(String(250))

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    role: Mapped["RoleModel"] = relationship(back_populates="users")
    feedback_id: Mapped[int] = mapped_column(ForeignKey("feedbacks.id"))
    feedback: Mapped[FeedbacksModel] = relationship(back_populates="users")