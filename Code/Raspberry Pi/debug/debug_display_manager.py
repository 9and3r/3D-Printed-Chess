import tkinter as tk
import threading
import time

from main.display_manager.display_manager_base import DisplayManagerBase


class DebugDisplayManager(DisplayManagerBase):

    def __init__(self):
        self.lock = threading.Lock()
        self.text1 = ""
        self.text2 = ""
        self.button_listener = None
        thread = threading.Thread(target=self.init_ui, args=())
        thread.start()
        time.sleep(1)

    def set_button_listener(self, listener):
        self.button_listener = listener

    def init_ui(self):
        self.main_window = tk.Tk()
        self.main_window.title("Display")
        self.main_window.geometry('+%d+%d' % (1100, 100))
        self.label1 = tk.Label(self.main_window, width=30, height=3)
        self.label1.grid(row=0, column=0, sticky="nsew", padx=1, pady=1, columnspan=3)
        self.label2 = tk.Label(self.main_window, width=30, height=3)
        self.label2.grid(row=1, column=0, sticky="nsew", padx=1, pady=1, columnspan=3)
        self.button_left = tk.Button(self.main_window, text="<-")
        self.button_left.grid(row=2, column=0, sticky="nsew", padx=1, pady=1)
        self.button_right = tk.Button(self.main_window, text="->")
        self.button_right.grid(row=2, column=2, sticky="nsew", padx=1, pady=1)
        self.button_select = tk.Button(self.main_window, text="OK")
        self.button_select.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)
        self.button_left.bind('<Button-1>', self.button_click)
        self.button_right.bind('<Button-1>', self.button_click)
        self.button_select.bind('<Button-1>', self.button_click)
        self.update()

    def show_message(self, line1, line2):
        self.text1 = line1
        self.text2 = line2

    def update(self):
        while True:
            with self.lock:
                self.label1.configure(text=self.text1)
                self.label2.configure(text=self.text2)
            self.main_window.update()

    def button_click(self, event):
        if event.widget == self.button_left:
            self.button_listener.left()
        elif event.widget == self.button_right:
            self.button_listener.right()
        elif event.widget == self.button_select:
            self.button_listener.select()