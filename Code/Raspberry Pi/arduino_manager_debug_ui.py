from tkinter import ttk
import tkinter as tk

class ArduinoManagerDebug(ttk.Frame):

    def __init__(self):
        main_window = tk.Tk()
        super().__init__(main_window)
        main_window.title("Combobox")

        self.combo = ttk.Combobox(self, state="readonly")
        self.combo.place(x=50, y=50)
        self.combo["values"] = ["w", "b", "-"]

        main_window.configure(width=300, height=200)
        self.place(width=300, height=200)
