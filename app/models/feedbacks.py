from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.products import ProductModel
    from app.models.users import UserModel

class FeedbacksModel(Base):
    __tablename__="feedbacks"

    id: Mapped[int] = mapped_column(primary_key=True)
    feedback: Mapped[str] = mapped_column(String(10000), nullable=False)

    user_id: Mapped[list["UserModel"]] = relationship(back_populates="feedback")
    product_id: Mapped[list["ProductModel"]] = relationship(back_populates="feedback")