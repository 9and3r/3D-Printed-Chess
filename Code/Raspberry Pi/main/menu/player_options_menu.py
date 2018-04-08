from main.menu.sub_menu import SubMenu
from main.game_manager import GameManager


class PlayerOptionsMenu(SubMenu):

    def __init__(self, current_player, parent, first_player=None, option_index=0):
        self.option = current_player.get_configuration_options()[option_index]
        self.current_player = current_player
        self.first_player = first_player
        self.parent = parent
        self.option_index = option_index
        values = []
        for value in self.option["values"]:
            values.append(value["name"])
        SubMenu.__init__(self, self.option["name"], values, parent=parent)

    def on_select_element(self, pos, element):
        self.current_player.configure_option(self.option["id"], self.option["values"][pos]["value"])
        # Check if it is the last option
        self.option_index += 1
        if len(self.current_player.get_configuration_options()) == self.option_index:
            # Last option
            if self.first_player is not None:
                GameManager.instance.new_game(player1=self.first_player, player2=self.current_player)
            else:
                # Go to next player select menu
                from main.menu.player_select_menu import PlayerSelectMenu
                self.elements = [PlayerSelectMenu(first_player=self.current_player, parent=self.parent)]
                self.current_pos = 0
                self.in_submenu = True
                self.elements[0].on_enter_submenu()
        else:
            # Go to next option
            self.elements = [PlayerOptionsMenu(self.current_player, self.parent, self.first_player, self.option_index)]
            self.current_pos = 0
            self.in_submenu = True
            self.elements[0].on_enter_submenu()
