from main.players.base_player import BasePlayer
from main.game_manager import GameManager


class HumanPlayer(BasePlayer):

    def get_player_name(self):
        return "Human player"

    def make_next_move(self):
        # Show possible moves
        self.board_manager.show_possible_pieces(self.game_manager.game.get_moves(player=self.color))

        # Esperar a que se levante una pieza
        initial_board_status = self.game_manager.wait_for_differences_in_board()

        # Calcular las posiciones que han cambiado
        current_board_status = self.board_manager.get_current_board_status()
        positions = GameManager.get_changed_positions(initial_board_status, current_board_status)

        # Comprobar que solo ha cambiado una posicion
        if len(positions) == 1:

            player = self.game_manager.game.board.get_owner(positions[0])
            possible_moves = self.game_manager.game.get_moves(idx_list=[positions[0]])
            if self.game_manager.game.board.get_owner(positions[0]) == player and len(possible_moves) > 0:
                # Find posible moves
                # Si la pieza es correcta mostrar los posibles movimientos
                self.board_manager.show_posible_moves(possible_moves)

                # Calculate valid boards
                valid_boards = {}
                for possible_move in possible_moves:
                    array = list(current_board_status)
                    array[GameManager.coordinate_to_int(possible_move[2:4])] = player
                    valid_boards[possible_move] = (''.join(array))

                # Esperar a que se realize el movimiento
                move = self.game_manager.wait_for_board_to_change_to(valid_boards, initial_board_status)
                if self.game_manager.game_running:
                    if move:
                        self.game_manager.game.apply_move(move)
                    else:
                        # Hemos vuelto a la posicion inicial. Volver a intentar
                        self.make_next_move()

                # Añadir el movimiento al juego si es valido que se actualice
            else:
                self.board_manager.show_error_positions(GameManager.int_positions_to_coordinates(positions))
        else:
            # Esperar a que el board este en modo correcto y volver a intentar
            self.game_manager.wait_for_differences_in_board()
            self.make_next_move()