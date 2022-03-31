from enum import IntEnum
from math import inf


class Color(IntEnum):
    WHITE = 1
    BLACK = 2


class Checkers:
    def __init__(self):
        width, height = 8, 8

        self.checkerboard = [[0] * width for _ in range(height)]

        self.place_checkers(Color.BLACK)
        self.place_checkers(Color.WHITE)

    def print_board(self):
        for i in self.checkerboard:
            for j in i:
                print(j, end=' ')
            print()

        print()

    def move_checker(self, start, end):
        start_x, start_y = start
        end_x, end_y = end

        checker = self.checkerboard[start_x][start_y]
        self.checkerboard[start_x][start_y] = 0
        self.checkerboard[end_x][end_y] = checker

    def place_checkers(self, color):
        if color == Color.BLACK:
            rows = range(5, 8)
            offset = 1
        else:
            rows = range(0, 3)
            offset = 0

        for i in rows:
            for j in range(offset, 8, 2):
                self.checkerboard[i][j] = int(color)

            offset = 1 if offset == 0 else 0


class AI:
    def __init__(self):
        self.difficulty = 0

    def minimax(self, board, depth, maximizing_player):
        if depth == 0 or game.game_over:
            return board.value

        if maximizing_player:
            max_eval = -inf
            for position in game.get_positions():
                eval = self.minimax(board, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = inf
            for position in game.get_positions():
                eval = self.minimax(board, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval


if __name__ == '__main__':
    game = Checkers()

    game.print_board()
    game.move_checker((2, 0), (3, 1))
    game.print_board()
