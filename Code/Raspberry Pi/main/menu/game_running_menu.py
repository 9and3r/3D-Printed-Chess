from main.menu.sub_menu import SubMenu

class GameRunningMenu(SubMenu):

    def __init__(self, game_manager):
        SubMenu.__init__(self, "Game", [""])
        self.player = 'w'
        self.game_manager = game_manager

    def game_changed(self, player):
        if player == 'w':
            self.name = "Turn: White"
        else:
            self.name = "Turn: Black"

        self.elements = ["Exit game"]

    def on_select_element(self, pos, element):
        if element == "Exit game":
            self.game_manager.stop_game()