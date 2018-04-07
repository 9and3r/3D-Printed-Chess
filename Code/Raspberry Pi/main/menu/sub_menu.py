class SubMenu:

    def __init__(self, name, elements, parent = None):
        self.elements = elements
        self.parent = parent
        self.name = name
        self.in_submenu = False
        if self.parent is None:
            self.current_pos = 0
        else:
            self.elements.insert(0, "<- Back")
            self.current_pos = 1

    def on_enter_submenu(self):
        if self.parent is None:
            self.current_pos = 0
        else:
            self.current_pos = 1

    def left(self):
        if self.in_submenu:
            self.elements[self.current_pos].left()
        else:
            self.current_pos -= 1
            if self.current_pos < 0:
                self.current_pos = 0

    def right(self):
        if self.in_submenu:
            self.elements[self.current_pos].right()
        else:
            self.current_pos += 1
            if self.current_pos == len(self.elements):
                self.current_pos -=1

    def get_name(self):
        if self.in_submenu:
            return self.elements[self.current_pos].get_name()
        else:
            return self.name

    def get_current_value(self):
        if isinstance(self.elements[self.current_pos], SubMenu):
            if self.in_submenu:
                return self.elements[self.current_pos].get_current_value()
            else:
                return self.elements[self.current_pos].name
        else:
            return self.elements[self.current_pos]

    def select(self):
        if self.in_submenu:
            self.elements[self.current_pos].select()
        else:
            if self.parent is not None and self.current_pos == 0:
                self.parent.exit_submenu()
            elif isinstance(self.elements[self.current_pos], SubMenu):
                self.elements[self.current_pos].on_enter_submenu()
                self.in_submenu = True
            else:
                self.on_select_element(self.current_pos, self.elements[self.current_pos])

    def exit_submenu(self):
        self.in_submenu = False

    def on_select_element(self, pos, element):
        pass


