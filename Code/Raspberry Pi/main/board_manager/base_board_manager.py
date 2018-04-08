class BaseBoardManager():

    def get_current_board_status(self):
        raise NotImplementedError('This method should be implemented')

    def clear_board(self):
        raise NotImplementedError('This method should be implemented')

    def show_possible_pieces(self, moves):
        raise NotImplementedError('This method should be implemented')

    def show_posible_moves(self, moves):
        raise NotImplementedError('This method should be implemented')

    def show_error_positions(self, errors):
        raise NotImplementedError('This method should be implemented')

    def show_AI_move(self, move):
        raise NotImplementedError('This method should be implemented')

    def show_AI_thinking(self):
        raise NotImplementedError('This method should be implemented')

    def standby(self):
        raise NotImplementedError('This method should be implemented')