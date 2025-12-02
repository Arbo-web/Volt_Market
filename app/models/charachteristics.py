from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.roles import ProductModel

class CharachteristicsModel(Base):
    __tablename__="charachteristics"
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    value: Mapped[str] = mapped_column(String(100), nullable=False)
    products_id: Mapped["ProductModel"] = relationship(back_populates="products")