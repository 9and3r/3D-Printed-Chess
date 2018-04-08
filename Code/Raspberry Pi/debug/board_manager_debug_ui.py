import tkinter as tk
import threading
import time
from main.board_manager.base_board_manager import BaseBoardManager
from main.game_manager import GameManager


class BoardManagerDebugUI(BaseBoardManager):

    def __init__(self):
        BaseBoardManager.__init__(self)
        self.lock = threading.Lock()
        self.board_data_string = "bbbbbbbbbbbbbbbb--------------------------------wwwwwwwwwwwwwwww"

    def start(self, game_manager):
        self.game_manager = game_manager
        thread = threading.Thread(target=self.init_ui, args=())
        thread.start()
        time.sleep(1)

    def init_ui(self):
        self.main_window = tk.Tk()
        self.main_window.title("Board input/output")
        self.main_window.geometry('+%d+%d' % (150, 100))

        self.secondary_window = tk.Tk()
        self.secondary_window.title("Board status")
        self.secondary_window.geometry('+%d+%d' % (600, 100))

        self.tiles = {}
        self.tileColors = {}
        self.board_data = list(self.board_data_string)

        self.tiles2 = []

        for i in range(0, 8):
            self.tiles[GameManager.letters_array[i]] = {}
            self.tileColors[GameManager.letters_array[i]] = {}
            for z in range(0, 8):
                tile = tk.Label(self.main_window, width=6, height=3)
                tile.bind('<Button-1>', self.buttonClick)
                tile.bind('<Button-2>', self.buttonClick)
                tile.bind('<Button-3>', self.buttonClick)
                tile.grid(row=z, column=i, sticky="nsew", padx=1, pady=1)
                tile.board_position = (z * 8) + i

                tile2 = tk.Label(self.secondary_window, width=6, height=3)
                tile2.grid(row=i, column=z, sticky="nsew", padx=1, pady=1)
                self.tiles2.append(tile2)

                self.tiles[GameManager.letters_array[i]][str(8 - z)] = tile
                self.tileColors[GameManager.letters_array[i]][str(8 - z)] = "gray"

                if z == 0 or z == 1:
                    text = "b"
                elif z == 6 or z == 7:
                    text = "w"
                else:
                    text = "-"

                tile.configure(text=text)

            self.board_data_string = ''.join(self.board_data)
        self.update()

    def show_possible_pieces(self, moves):
        with self.lock:
            self.clear_board()
            for move in moves:
                key1 = move[0:1]
                key2 = move[1:2]
                self.tileColors[key1][key2] = "blue"

    def show_posible_moves(self, moves):
        with self.lock:
            self.clear_board()
            for move in moves:
                self.tileColors[move[0:1]][move[1:2]] = "blue"
                key1 = move[2:3]
                key2 = move[3:4]
                self.tileColors[key1][key2] = "green"

    def show_AI_move(self, move):
        with self.lock:
            self.clear_board()
            start_key1 = move[0:1]
            start_key2 = move[1:2]
            target_key1 = move[2:3]
            target_key2 = move[3:4]
            self.tileColors[start_key1][start_key2] = "blue"
            self.tileColors[target_key1][target_key2] = "green"

    def show_AI_thinking(self):
        with self.lock:
            self.clear_board()

    def show_error_positions(self, errors):
        with self.lock:
            self.clear_board()
            for error in errors:
                key1 = error[0:1]
                key2 = error[1:2]
                self.tileColors[key1][key2] = "red"

    def get_current_board_status(self):
        with self.lock:
            return self.board_data_string

    def update(self):
        while True:
            # Update colors
            with self.lock:
                for key1 in self.tileColors:
                    for key2 in self.tileColors[key1]:
                        self.tiles[key1][key2].configure(background=self.tileColors[key1][key2])
            self.main_window.update()
            self.secondary_window.update()

            positions = self.game_manager.game.board._position
            i = 0
            for tile in self.tiles2:
                text = positions[i]
                if len(text.strip()) == 0:
                    tile.configure(background="gray")
                elif text.isupper():
                    tile.configure(background="white", foreground="black")
                else:
                    tile.configure(background="black", foreground="white")
                tile.configure(text=text)
                i += 1

    def clear_board(self):
        for key1 in self.tileColors:
            for key2 in self.tileColors[key1]:
                self.tileColors[key1][key2]="gray"

    def standby(self):
        self.clear_board()

    def buttonClick(self, event):
        with self.lock:
            if event.num == 1:
                text = "w"
            elif event.num == 2:
                text = "-"
            elif event.num == 3:
                text = "b"
            event.widget.configure(text=text)
            self.board_data[event.widget.board_position] = text
            self.board_data_string = ''.join(self.board_data)
