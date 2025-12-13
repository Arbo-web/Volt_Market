from pydantic import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.schemes.users import SUserGet
    from app.schemes.products import SProductGet


class SFeedbackAdd(BaseModel):
    feedback: str
    user_id: int
    product_id: int


class SFeedbackGet(BaseModel):
    id: int
    feedback: str
    user_id: int
    product_id: int


class SFeedbackUpdate(BaseModel):
    feedback: str | None = None