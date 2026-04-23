from repositories.base_repository import BaseRepository
from models.system.menu import Menu


class MenuRepository(BaseRepository):
    def __init__(self):
        super().__init__(Menu, allowed_fields=[c.name for c in Menu.__table__.columns])

    def _to_dict(self, obj):

        if isinstance(obj, dict):
            return obj

        if hasattr(obj, "__table__"):
            return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

        return obj
