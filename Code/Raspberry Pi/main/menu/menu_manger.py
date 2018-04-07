from main.menu.main_menu import MainMenu

class MenuManager:

    def __init__(self, display_manager, game_manager):
        self.display_manager = display_manager
        self.game_manager = game_manager
        self.menu = MainMenu()

    def start(self):
        self.update_display()

    def update_display(self):
        line1 = self.menu.get_name()
        line2 = self.menu.get_current_value()
        self.display_manager.show_message(line1, line2)

    def left(self):
        self.menu.left()
        self.update_display()

    def right(self):
        self.menu.right()
        self.update_display()

    def select(self):
        self.menu.select()
        self.update_display()




