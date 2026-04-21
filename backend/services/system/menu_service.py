from repositories.system.menu_repository import MenuRepository


class MenuClass:
    def __init__(self):
        self.repo = MenuRepository()

    def get_menu_list(self, db, data):
        pass
