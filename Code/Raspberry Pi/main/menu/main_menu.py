from main.menu.sub_menu import SubMenu
from main.menu.network_submenu import NetworkMenu

class MainMenu(SubMenu):

    def __init__(self):
        SubMenu.__init__(self, "Main menu", ["New game", "Load game", NetworkMenu(self), "Shutdown"])
