from main.menu.main_menu import MainMenu
from main.menu.game_running_menu import GameRunningMenu

class MenuManager:

    instance = None

    def __init__(self, display_manager):
        MenuManager.instance = self
        self.display_manager = display_manager
        self.menu = None

    def start(self):
        self.menu = MainMenu()
        self.update_display()

    def update_display(self):
        line1 = self.menu.get_name()
        line2 = self.menu.get_current_value()
        self.display_manager.show_message(line1, line2)

    def left(self):
        self.menu.left()
        self.update_display()

    def right(self):
        self.menu.right()
        self.update_display()

    def select(self):
        self.menu.select()
        self.update_display()

    def set_game_running(self, game_manager, running):
        if running:
            self.menu = GameRunningMenu(game_manager)
        else:
            self.menu = MainMenu()
        self.update_display()

    def game_status_changed(self, player):
        self.menu.game_changed(player)
        self.update_display()
