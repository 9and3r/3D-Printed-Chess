from main.menu.main_menu import MainMenu
from main.menu.game_running_menu import GameRunningMenu

from chessnut.game import Game

class MenuManager:

    instance = None

    def __init__(self, display_manager):
        MenuManager.instance = self
        self.display_manager = display_manager
        self.menu = None
        self.game_finished = False

    def start(self):
        self.menu = MainMenu()
        self.update_display()

    def update_display(self):
        line1 = self.menu.get_name()
        line2 = self.menu.get_current_value()
        self.display_manager.show_message(line1, line2)

    def left(self):
        if self.check_input_game_finished():
            self.menu.left()
        self.update_display()

    def right(self):
        if self.check_input_game_finished():
            self.menu.right()
        self.update_display()

    def select(self):
        if self.check_input_game_finished():
            self.menu.select()
        self.update_display()

    def check_input_game_finished(self):
        if self.game_finished:
            self.menu = MainMenu()
            self.game_finished = False
            return False
        else:
            return True

    def set_game_running(self, game_manager, running):
        if running:
            self.menu = GameRunningMenu(game_manager)
        else:
            self.menu = MainMenu()
        self.update_display()

    def game_status_changed(self, player):
        self.menu.game_changed(player)
        self.update_display()

    def game_finished(self, player, state):
        self.game_finished = True
        if state == Game.STALEMATE:
            self.display_manager.show_message("Game finished", "Stalemate")
        else:
            if player == "w":
                self.display_manager.show_message("Game finished", "Black wins")
            else:
                self.display_manager.show_message("Game finished", "White wins")
