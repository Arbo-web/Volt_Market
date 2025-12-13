from pydantic import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.schemes.characteristics import SCharacteristicGet
    from app.schemes.feedbacks import SFeedbackGet


class SProductAdd(BaseModel):
    name: str
    description: str | None = None
    image_url: str
    cost: int
    quantity: int
    characteristic_id: int


class SProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    image_url: str | None = None
    cost: int | None = None
    quantity: int | None = None
    characteristic_id: int | None = None


class SProductGet(SProductAdd):
    id: int


class SProductGetWithFeedbacks(SProductGet):
    characteristic: "SCharacteristicGet"
    feedbacks: list["SFeedbackGet"] | None = []