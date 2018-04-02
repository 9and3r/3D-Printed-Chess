class BasePlayer:

    def __init__(self):
        self.color = 'w'
        self.game_manager = None
        self.board_manager = None

    def set_params(self, game_manager, board_manager, color):
        self.color = color
        self.game_manager = game_manager
        self.board_manager = board_manager

    def get_player_name(self):
        raise NotImplementedError('This method should be implemented')

    def make_next_move(self):
        raise NotImplementedError('This method should be implemented')