from enum import IntEnum
from math import inf
from copy import deepcopy


class Color(IntEnum):
    WHITE = 1
    BLACK = 2


class Piece:
    def __init__(self, row, column, color):
        self.color = color
        self.row = row
        self.col = column
        self.king = False


class Checkerboard:
    def __init__(self):
        width, height = 8, 8

        self.board = [[0] * width for _ in range(height)]

        self.place_checkers(Color.BLACK)
        self.place_checkers(Color.WHITE)

    def draw(self):
        for i in self.board:
            for j in i:
                print(j, end=' ')
            print()

        print()

    def move_checker(self, start, end):
        start_x, start_y = start
        end_x, end_y = end

        checker = self.board[start_x][start_y]
        self.board[start_x][start_y] = 0
        self.board[end_x][end_y] = checker

    def place_checkers(self, color):
        if color == Color.BLACK:
            rows = range(5, 8)
            offset = 1
        else:
            rows = range(0, 3)
            offset = 0

        for i in rows:
            for j in range(offset, 8, 2):
                self.board[i][j] = int(color)

            offset = 1 if offset == 0 else 0


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
            for position in self.get_moves():
                eval = self.minimax(board, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)

                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_moves(self):
        moves = []
        # TODO game.get_board()
        board = game

        for piece in board.get_pieces():
            for move in board.get_moves(piece):
                board_copy = deepcopy(board)
                piece_copy = board_copy.get_piece(piece.row, piece.col)

                board_copy.move()


if __name__ == '__main__':
    game = Checkerboard()

    game.draw()
    game.move_checker((2, 0), (3, 1))
    game.draw()
