import os

from main.menu.sub_menu import SubMenu
from main.menu.network_submenu import NetworkMenu
from main.menu.player_select_menu import PlayerSelectMenu


class MainMenu(SubMenu):

    def __init__(self):
        SubMenu.__init__(self, "Main menu", [PlayerSelectMenu(parent=self), "Load game", NetworkMenu(self), "Shutdown"])

    def on_select_element(self, pos, element):
        if element == "Shutdown":
            os.system("sudo shutdown -h now")
