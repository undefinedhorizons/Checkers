from color import Color
from piece import Piece


class Checkerboard:
    def __init__(self):
        self.rows, self.cols = 8, 8

        self.board = [[0] * self.cols for _ in range(self.rows)]

        self.place_pieces(Color.BLACK)
        self.place_pieces(Color.WHITE)

        self.white_left = 12
        self.black_left = 12

        self.white_kings = 0
        self.black_kings = 0

    def remove(self, pieces):
        for piece in pieces:

            self.board[piece.row][piece.col] = 0

            if piece != 0:
                if piece.color == Color.BLACK:
                    self.black_left -= 1
                else:
                    self.white_left -= 1

    def draw(self):
        for i in self.board:
            for j in i:
                print(j, end=' ')
            print()

        print()

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row=row, col=col)

        if not piece.is_king():
            if row == self.rows and piece.color == Color.WHITE:
                piece.set_king()
                self.white_kings += 1

            if row == 0 and piece.color == Color.BLACK:
                piece.set_king()
                self.black_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def place_pieces(self, color):
        if color == Color.BLACK:
            rows = range(5, 8)
            offset = 1
        else:
            rows = range(0, 3)
            offset = 0

        for i in rows:
            for j in range(offset, 8, 2):
                piece = Piece(row=i, col=j, color=color)
                self.board[i][j] = piece

            offset = 1 if offset == 0 else 0
