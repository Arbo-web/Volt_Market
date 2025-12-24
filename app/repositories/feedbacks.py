from app.models.feedbacks import FeedbacksModel
from app.repositories.base import BaseRepository
from app.schemes.feedbacks import SFeedbackGet

class ProductsRepository(BaseRepository):
    model = FeedbacksModel
    schema = SFeedbackGet