from main.players.base_player import BasePlayer
from main.game_manager import GameManager


class HumanPlayer(BasePlayer):

    def get_player_name(self):
        return "Human"

    def get_configuration_options(self):
        return []

    def make_next_move(self):
        # Show possible moves
        self.board_manager.show_possible_pieces(self.game_manager.game.get_moves(player=self.color))

        # Wait until a piece is taken out from the board
        initial_board_status = self.game_manager.wait_for_differences_in_board()

        # Check what positions have changed
        current_board_status = self.board_manager.get_current_board_status()
        positions = GameManager.get_changed_positions(initial_board_status, current_board_status)

        # Only one position should have changed
        if len(positions) == 1:

            player = self.game_manager.game.board.get_owner(positions[0])
            possible_moves = self.game_manager.game.get_moves(idx_list=[positions[0]])

            # Check that in the changed position there was a piece of this player
            # Check that this piece has one or more valid moves
            if self.game_manager.game.board.get_owner(positions[0]) == player and len(possible_moves) > 0:

                # Show the valid moves
                self.board_manager.show_posible_moves(possible_moves)

                # Calculate valid boards after making each of the valid moves
                valid_boards = {}
                for possible_move in possible_moves:
                    array = list(current_board_status)
                    array[GameManager.coordinate_to_int(possible_move[2:4])] = player
                    valid_boards[possible_move] = (''.join(array))

                # Wait until some of the moves is done or
                # the move is canceled by putting the piece on this turn initial position
                move = self.game_manager.wait_for_board_to_change_to(valid_boards, initial_board_status)
                if self.game_manager.game_running:
                    if move:

                        # A valid move was detected. Apply that move
                        self.game_manager.confirm_move(move)
                    elif self.game_manager.game_running:
                        # Hemos vuelto a la posicion inicial. Volver a intentar
                        self.make_next_move()
            else:
                self.board_manager.show_error_positions(GameManager.int_positions_to_coordinates(positions))
                # todo esperar a que el board este en el estado esperado
                self.make_next_move()
        elif self.game_manager.game_running:
            # Wait until the board is on this turin initial position and try again
            self.game_manager.wait_for_differences_in_board()
            self.make_next_move()