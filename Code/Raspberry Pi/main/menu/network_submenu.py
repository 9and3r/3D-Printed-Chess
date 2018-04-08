import socket
from main.menu.sub_menu import SubMenu


class NetworkMenu(SubMenu):

    def __init__(self, parent):
        ips = [socket.gethostbyname(socket.gethostname())]
        SubMenu.__init__(self, "IP address", elements=ips, parent=parent)