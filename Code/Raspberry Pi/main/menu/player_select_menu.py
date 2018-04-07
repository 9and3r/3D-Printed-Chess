from main.game_manager import GameManager
from main.menu.sub_menu import SubMenu
from main.players.human_player import HumanPlayer
from main.players.stockfish_player import StockfishPlayer


class PlayerSelectMenu(SubMenu):

    PlayerTypes = [HumanPlayer, StockfishPlayer]

    def __init__(self, first_player=None, parent=None):
        self.first_player = first_player
        if first_player is None:
            menu_name = "White player"
        else:
            menu_name = "Black player"

        player_type_names = []
        for player_type in PlayerSelectMenu.PlayerTypes:
            player_type_names.append(player_type.__name__)
        SubMenu.__init__(self, "New game", player_type_names, parent=parent, name_inside=menu_name)

    def on_select_element(self, pos, element):
        if self.first_player is None:
            self.elements = [PlayerSelectMenu(first_player=PlayerSelectMenu.PlayerTypes[pos-1](), parent=self)]
            self.current_pos = 0
            self.in_submenu = True
            self.elements[0].on_enter_submenu()
        else:
            GameManager.instance.new_game(player1=self.first_player, player2=PlayerSelectMenu.PlayerTypes[pos-1]())


