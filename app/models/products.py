from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.characteristics import CharacteristicsModel
    from app.models.feedbacks import FeedbacksModel

class ProductModel(Base):
    __tablename__="products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(2000))
    image_url: Mapped[str] = mapped_column(String(250), nullable=False)
    cost: Mapped[int] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)

    characteristic_id: Mapped[int] = mapped_column(ForeignKey("characteristics.id"), nullable=False)
    characteristic: Mapped["CharacteristicsModel"] = relationship(back_populates="products")
    
    feedbacks: Mapped[list["FeedbacksModel"]] = relationship(back_populates="product")