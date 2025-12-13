from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.products import ProductModel

class CharacteristicsModel(Base):
    __tablename__ = "characteristics"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    value: Mapped[str] = mapped_column(String(100), nullable=False)

    products: Mapped[list["ProductModel"]] = relationship(back_populates="characteristic")