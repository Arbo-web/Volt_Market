from app.models.characteristics import CharacteristicsModel
from app.repositories.base import BaseRepository
from app.schemes.characteristics import SCharacteristicGet

class ProductsRepository(BaseRepository):
    model = CharacteristicsModel
    schema = SCharacteristicGet