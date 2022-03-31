from copy import deepcopy
from math import inf

from main import game


class AI:
    def __init__(self):
        self.difficulty = 0

    # minimax algorithm with pruning
    def minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or game.game_over:
            return board.value

        if maximizing_player:
            max_eval = -inf
            for move in self.get_moves():
                eval = self.minimax(board, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = inf
            for move in self.get_moves():
                eval = self.minimax(board, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)

                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_moves(self):
        moves = []
        board = game.board

        for piece in board.get_pieces():
            for move in board.get_moves(piece):
                board_copy = deepcopy(board)
                piece_copy = board_copy.get_piece(piece.row, piece.col)

                board_copy.move()