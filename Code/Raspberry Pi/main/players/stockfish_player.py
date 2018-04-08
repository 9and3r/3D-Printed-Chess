import subprocess

from main.players.base_player import BasePlayer
from main.game_manager import GameManager


class StockfishPlayer(BasePlayer):

    def __init__(self):
        super(StockfishPlayer).__init__()
        self.stockfish = subprocess.Popen(
            'stockfish',universal_newlines=True,
             stdin=subprocess.PIPE,
             stdout=subprocess.PIPE)
        self.send_command('uci')
        self.read_until('uciok')

    def read_until(self, response_start):
        found = False
        while not found:
            line = self.stockfish.stdout.readline().rstrip()
            if line.startswith(response_start):
                found = True
        if found:
            return line
        else:
            return None

    def send_command(self, command):
        self.stockfish.stdin.write(command)
        self.stockfish.stdin.write("\n")
        self.stockfish.stdin.flush()

    def get_player_name(self):
        return "Stockfish"

    def get_configuration_options(self):
        return [
            {"id":1, "name": "Difficulty", "values": [
                {"value": 0, "name": "Very easy"},
                {"value": 2, "name": "Easy"},
                {"value": 5, "name": "Medium"},
                {"value": 8, "name": "Hard"},
                {"value": 12, "name": "Expert"},
                {"value": 20, "name": "Impossible"},
            ]},
        ]

    def configure_option(self, option_id, value):
        if option_id == 1:
            self.send_command('setoption name Skill Level value ' + str(value))

    def make_next_move(self):

        self.board_manager.show_AI_thinking()

        # Give the current position to Stockfish
        fen = self.game_manager.game.get_fen()
        self.send_command('position fen ' + fen)

        # Tell Stockfish to think it's next move
        self.send_command('go')

        # Get Stockfish desired move
        move = StockfishPlayer.get_best_move(self.read_until('bestmove'))

        # Show the desired move in the board
        self.board_manager.show_AI_move(move)

        # Calculate the target board status
        valid_boards = {}
        array = list(self.game_manager.get_board_as_bw_string())
        array[GameManager.coordinate_to_int(move[0:2])] = '-'
        array[GameManager.coordinate_to_int(move[2:4])] = self.color
        valid_boards[move] = (''.join(array))

        # Wait until the move is done
        if self.game_manager.wait_for_board_to_change_to(valid_boards) == move:

            # Confirm the move
            if self.game_manager.game_running:
                self.game_manager.confirm_move(move)

        # Something went wrong. Try again
        elif self.game_manager.game_running:
            self.make_next_move()

    @staticmethod
    def get_best_move(line):
        lines = line.split(' ')
        return lines[1]