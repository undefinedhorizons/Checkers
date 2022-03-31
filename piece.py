class Piece:
    def __init__(self, row, col, color):
        self.color = color
        self.row, self.col = row, col

        self.king = False

    def set_king(self):
        self.king = True

    def is_king(self):
        return self.king

    def move(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return str(int(self.color))