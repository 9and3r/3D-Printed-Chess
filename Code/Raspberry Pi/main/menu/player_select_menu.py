from main.game_manager import GameManager
from main.menu.sub_menu import SubMenu
from main.players.human_player import HumanPlayer
from main.players.stockfish_player import StockfishPlayer
from main.menu.player_options_menu import PlayerOptionsMenu

class PlayerSelectMenu(SubMenu):

    PlayerTypes = [HumanPlayer, StockfishPlayer]

    def __init__(self, first_player=None, parent=None):
        self.first_player = first_player
        if first_player is None:
            menu_name = "White player"
        else:
            menu_name = "Black player"

        self.player_type_names = []
        for player_type in PlayerSelectMenu.PlayerTypes:
            self.player_type_names.append(player_type.__name__)
        SubMenu.__init__(self, "New game", self.player_type_names, parent=parent, name_inside=menu_name)

    def on_enter_submenu(self):
        super(PlayerSelectMenu, self).on_enter_submenu()
        self.elements = self.player_type_names
        self.current_pos = 1
        self.in_submenu = False

    def on_select_element(self, pos, element):
        current_player = PlayerSelectMenu.PlayerTypes[pos]()
        if len(current_player.get_configuration_options()) > 0:
            self.elements = [PlayerOptionsMenu(current_player, self.parent, first_player=self.first_player)]
            self.current_pos = 0
            self.in_submenu = True
            self.elements[0].on_enter_submenu()
        else:
            if self.first_player is None:
                self.elements = [PlayerSelectMenu(first_player=current_player, parent=self.parent)]
                self.current_pos = 0
                self.in_submenu = True
                self.elements[0].on_enter_submenu()
            else:
                GameManager.instance.new_game(player1=self.first_player, player2=current_player)


