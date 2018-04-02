import time
from chessnut.game import Game


class GameManager:

    letters_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    letter_to_position = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    letters_positions = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h'}

    def __init__(self, board_manager, player1, player2):
        self.board_manager = board_manager
        self.game_running = False
        self.current_player = 'w'
        player1.set_params(self, board_manager, 'w')
        player2.set_params(self, board_manager, 'b')
        self.game = Game()
        self.players = {'w': player1, 'b': player2}

    def start_game(self):
        self.game.reset()
        self.game_running = True
        self.current_player = 'w'
        while self.game_running:

            # Wait to set initial positions
            self.wait_and_show_errors(self.get_board_as_bw_string())

            # Make next move
            if self.game_running:
                self.players[self.current_player].make_next_move()

            # Change player
            if self.current_player == 'w':
                self.current_player = 'b'
            else:
                self.current_player = 'w'

    def stop_game(self):
        self.game_running = False

    def wait_for_differences_in_board(self):
        initial_board_state = self.board_manager.get_current_board_status()
        while initial_board_state == self.board_manager.get_current_board_status():
            time.sleep(0.05)
        return initial_board_state

    def wait_and_show_errors(self, target_board):
        while target_board != self.board_manager.get_current_board_status() and self.game_running:
            positions = self.get_changed_positions(target_board, self.board_manager.get_current_board_status())
            self.board_manager.show_error_positions(GameManager.int_positions_to_coordinates(positions))
            time.sleep(0.05)

    # waits until the board goes to one of the possible boards or returns to the previous_board_state
    # it returns the key of the possible board that matches the current status
    #  Returns false if the board has changed to previous_board_state
    def wait_for_board_to_change_to(self, possible_boards, previous_board_state = None):
        finish = False
        found = False
        while not finish and self.game_running:
            new_board_state = self.board_manager.get_current_board_status()
            for key in possible_boards:
                if possible_boards[key] == new_board_state:
                    found = key
                    finish = True
            if not found:
                if previous_board_state is not None and new_board_state == previous_board_state:
                    finish = True
                else:
                    time.sleep(0.05)
        return found

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



