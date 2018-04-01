import time
from game import Game


class GameManager:

    letters_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    letter_to_position = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    letters_positions = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h'}

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
            positions = self.get_changed_positions(target_board, self.arduino.get_current_board_status())
            self.arduino.show_error_positions(GameManager.int_positions_to_coordinates(positions))
            time.sleep(0.05)

    # waits until the board goes to one of the possible boards or returns to the previous_board_state
    # it returns the key of the possible board that matches the current status
    #  Returns false if the board has changed to previous_board_state
    def wait_for_board_to_change_to(self, possible_boards, previous_board_state):
        initial_board_state = self.arduino.get_current_board_status()
        finish = False
        found = False
        while not finish and self.game_running:
            new_board_state = self.arduino.get_current_board_status()
            for key in possible_boards:
                if possible_boards[key] == new_board_state:
                    found = key
                    finish = True
            if not found:
                if new_board_state == previous_board_state:
                    finish = True
                else:
                    time.sleep(0.05)
        return found


    def make_next_move_human_player(self, player):

        # Show possible moves
        self.arduino.show_possible_pieces(self.game.get_moves(player=player))

        # Esperar a que se levante una pieza
        initial_board_status = self.wait_for_differences_in_board()

        # Calcular las posiciones que han cambiado
        current_board_status = self.arduino.get_current_board_status()
        positions = GameManager.get_changed_positions(initial_board_status, current_board_status)

        # Comprobar que solo ha cambiado una posicion
        if len(positions) == 1:

            player = self.game.board.get_owner(positions[0])
            possible_moves = self.game.get_moves(idx_list=[positions[0]])
            if self.game.board.get_owner(positions[0]) == player and len(possible_moves) > 0:
                # Find posible moves
                # Si la pieza es correcta mostrar los posibles movimientos
                self.arduino.show_posible_moves(possible_moves)

                # Calculate valid boards
                valid_boards = {}
                for possible_move in possible_moves:
                    array = list(current_board_status)
                    array[GameManager.coordinate_to_int(possible_move[2:4])] = player
                    valid_boards[possible_move]= (''.join(array))

                # Esperar a que se realize el movimiento
                move = self.wait_for_board_to_change_to(valid_boards, initial_board_status)
                if self.game_running:
                    if move:
                        self.game.apply_move(move)
                    else:
                        # Hemos vuelto a la posicion inicial. Volver a intentar
                        self.make_next_move_human_player(player)

                # Añadir el movimiento al juego si es valido que se actualice
            else:
                self.arduino.show_error_positions(GameManager.int_positions_to_coordinates(positions))
        else:
            # Esperar a que el board este en modo correcto y volver a intentar
            self.wait_for_differences_in_board()
            self.make_next_move_human_player(player)

    def get_board_as_bw_string(self):
        current_board = ""

        for value in self.game.board._position:
            if len(value.strip()) > 0:
                if value.isupper():
                    current_board += 'w'
                else:
                    current_board += 'b'
            else:
                current_board += '-'
        return current_board


    @staticmethod
    def get_changed_positions(board1, board2):
        if board1 != board2:
            positions = []
            board1List = list(board1)
            board2List = list(board2)
            for i in range(0, len(board1)):
                if board1List[i] != board2List[i]:
                    positions.append(i)
            return positions
        else:
            return []

    @staticmethod
    def coordinate_to_int(coordinate):
        key1 = GameManager.letter_to_position[coordinate[0:1]]
        key2 = 8 * (8 - int(coordinate[1:2]))
        return key1+key2

    @staticmethod
    def int_positions_to_coordinates(positions):
        coordinates = []
        for position in positions:
            key1 = GameManager.letters_positions[str(position % 8)]
            key2 = str(8 - (position // 8))
            coordinates.append(key1 + key2)
        return coordinates



