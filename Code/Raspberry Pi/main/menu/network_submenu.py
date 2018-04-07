import socket
from main.menu.sub_menu import SubMenu


class NetworkMenu(SubMenu):

    def __init__(self, parent):
        adapters = socket.getaddrinfo(socket.gethostname(), None)
        ips = ["192.168.1.110"]
        SubMenu.__init__(self, "IP address", elements=ips, parent=parent)