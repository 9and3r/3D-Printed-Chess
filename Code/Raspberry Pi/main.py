from main.game_manager import GameManager
from debug.board_manager_debug_ui import BoardManagerDebugUI
from main.players.human_player import HumanPlayer
from main.players.stockfish_player import StockfishPlayer



manager = BoardManagerDebugUI()

game_manager = GameManager(manager, HumanPlayer(), StockfishPlayer())
manager.start(game_manager)
game_manager.start_game()