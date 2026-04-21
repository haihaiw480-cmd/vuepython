from repositories.system.menu_repository import MenuRepository


class MenuService:
    def __init__(self):
        self.repo = MenuRepository()

    def get_menu_list(self, db, data=None):
        return {'000'}
