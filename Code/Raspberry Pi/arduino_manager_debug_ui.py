import tkinter as tk
import threading
import time
from game_manager import GameManager


class ArduinoManagerDebug():

    def __init__(self):
        self.lock = threading.Lock()
        self.board_data_string = "bbbbbbbbbbbbbbbb--------------------------------wwwwwwwwwwwwwwww"
        thread = threading.Thread(target=self.init_ui, args=())
        thread.start()
        time.sleep(1)

    def init_ui(self):
        self.main_window = tk.Tk()
        self.main_window.title("Chess Board")
        self.tiles = {}
        self.tileColors = {}
        self.board_data = list(self.board_data_string)

        for i in range(0, 8):
            self.tiles[GameManager.letters_array[i]] = {}
            self.tileColors[GameManager.letters_array[i]] = {}
            for z in range(0, 8):
                tile = self.combo = tk.Button(self.main_window, width=2)
                tile.bind('<Button-1>', self.buttonClick)
                tile.bind('<Button-2>', self.buttonClick)
                tile.bind('<Button-3>', self.buttonClick)
                tile.grid(row=z, column=i, sticky="nsew", padx=1, pady=1)
                tile.board_position = (z * 8) + i

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
                key1 = move[2:3]
                key2 = move[3:4]
                self.tileColors[key1][key2] = "green"

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

    def clear_board(self):
        for key1 in self.tileColors:
            for key2 in self.tileColors[key1]:
                self.tileColors[key1][key2]="gray"

    def buttonClick(self, event):
        for key1 in self.tiles:
            for key2 in self.tiles[key1]:
                if self.tiles[key1][key2] == event.widget:
                    print(key1 + key2)

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
