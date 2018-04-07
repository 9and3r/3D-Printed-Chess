from main.game_manager import GameManager
from debug.board_manager_debug_ui import BoardManagerDebugUI
from debug.debug_display_manager import DebugDisplayManager
from main.menu.menu_manger import MenuManager




display_manager = DebugDisplayManager()
board_manager = BoardManagerDebugUI()
game_manager = GameManager(board_manager)
board_manager.start(game_manager)
menu_manager = MenuManager(display_manager, game_manager)
display_manager.set_button_listener(menu_manager)
menu_manager.start()

