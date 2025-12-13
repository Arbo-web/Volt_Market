from pydantic import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.schemes.products import SProductGet


class SCharacteristicAdd(BaseModel):
    name: str
    value: str


class SCharacteristicUpdate(BaseModel):
    name: str | None = None
    value: str | None = None


class SCharacteristicGet(SCharacteristicAdd):
    id: int


class SCharacteristicGetWithProducts(SCharacteristicGet):
    products: list["SProductGet"] | None = []