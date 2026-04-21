from repositories.base_repository import BaseRepository
from models.system.menu import Menu


class MenuRepository(BaseRepository):
    def __init__(self):
        super().__init__(Menu, allowed_fields=[])
