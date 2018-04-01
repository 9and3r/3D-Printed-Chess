from main.game_manager import GameManager
from debug.arduino_manager_debug_ui import ArduinoManagerDebug
from main.players.human_player import HumanPlayer
manager = ArduinoManagerDebug()

game_manager = GameManager(manager, HumanPlayer(), HumanPlayer())
game_manager.start_game()


from chessnut.game import Game

chessgame = Game()
print(chessgame)

game_running = True








print(chessgame.get_moves())
#chessgame.apply_move(chessgame.get_moves()[0])
for i in range(64):
    print(chessgame.get_moves('b8'))
chessgame.apply_move(chessgame.get_moves()[0])
print(chessgame.get_moves())