from repositories.base_repository import BaseRepository
from models.system.user import User


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User, allowed_fields={c.name for c in User.__table__.columns})
