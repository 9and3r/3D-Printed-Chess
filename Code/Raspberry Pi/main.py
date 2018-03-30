
from arduino_manager_debug_ui import ArduinoManagerDebug
manager = ArduinoManagerDebug()
manager.mainloop()

from game import Game

chessgame = Game()
print(chessgame)

game_running = True








print(chessgame.get_moves())
#chessgame.apply_move(chessgame.get_moves()[0])
for i in range(64):
    print(chessgame.get_moves('b8'))
chessgame.apply_move(chessgame.get_moves()[0])
print(chessgame.get_moves())