import time
from game import Game


class GameManager:

    def __init__(self, arduino_manager):
        self.arduino = arduino_manager
        self.game_running = False
        self.current_player = 'w'
        self.game = Game()

    def start_game(self):
        self.game.reset()
        self.game_running = True
        self.current_player = 'w'
        while self.game_running:

            # Wait to set initial positions
            self.wait_and_show_errors(self.get_board_as_bw_string())

            # Make next move
            if self.game_running:
                self.make_next_move_human_player(self.current_player)

            # Change player
            if self.current_player == 'w':
                self.current_player = 'b'
            else:
                self.current_player = 'w'

    def stop_game(self):
        self.game_running = False

    def wait_for_differences_in_board(self):
        initial_board_state = self.arduino.get_current_board_status()
        while initial_board_state == self.arduino.get_current_board_status():
            time.sleep(0.05)
        return initial_board_state

    def wait_and_show_errors(self, target_board):
        while target_board != self.arduino.get_current_board_status() and self.game_running:
            # TODO MOSTRAR ERRORES de las posiciones
            positions = self.get_changed_positions(target_board, self.arduino.get_current_board_status())
            time.sleep(0.05)

    def make_next_move_human_player(self, player):

        # Esperar a que se levante una pieza
        initial_board_status = self.wait_for_differences_in_board()
        positions = GameManager.get_changed_positions(initial_board_status, self.arduino.get_current_board_status())

        if len(positions) == 1 and self.game.board.get_owner(positions[0]) == player:
            # Find posible moves
                # Si la pieza es correcta mostrar los posibles movimientos
                self.arduino.show_posible_moves(self.game.get_moves(idx_list="a8"))

                # Comprobar si una pieza vuelve al tablero o otra desaparce (Si desaparece ha comido otra pieza)
                # Comprobar que el movimiento es uno de los validos

                # Añadir el movimiento al juego si es valido que se actualice
        else:
            # Esperar a que el board este en modo correcto y volver a intentar
            self.wait_for_differences_in_board(self.get_board_as_bw_string())
            self.make_next_move_human_player(player)

    def get_board_as_bw_string(self):
        current_board = ""
        for value in self.game.board:
            if len(value.trim()) > 0:
                if value.isupper(value):
                    current_board += 'b'
                else:
                    current_board += 'w'
            else:
                current_board += '0'
        return current_board


    @staticmethod
    def get_changed_positions(board1, board2):
        if board1 != board2:
            positions = []
            board1List = list(board1)
            board2List = list(board2)
            for i in range(0, len(board1)):
                if board1List[i] == board2List[i]:
                    positions.push(i)
            return positions
        else:
            return []




