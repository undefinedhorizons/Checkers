from board import Checkerboard
from color import Color

class Game:
    def __init__(self):
        self.board = Checkerboard()
        self.moves = {}
        self.turn = Color.WHITE

    def draw(self):
        self.board.draw()

    def move(self, piece, row, col):
        self._move(piece, row, col)

    def _move(self, piece, row, col):
        other_piece = self.board.get_piece(row, col)
        if other_piece == 0 and (row, col) in self.moves:
            self.board.move(piece, row, col)
            skipped = self.moves[(row, col)]
            if skipped:
                self.moves = self.moves.pop(skipped)
            self.next_turn()

    def next_turn(self):
        self.moves = {}
        self.turn = Color.BLACK if Color.WHITE else Color.WHITE

    def get_moves(self, piece):
        moves = {}
        left_pos = piece.col - 1
        right_pos = piece.col + 1
        row = piece.row

        if piece.color == Color.BLACK or piece.is_king():
            moves.update(self._move_left(row - 1, max(row - 3, -1), -1, piece.color, left_pos))
            moves.update(self._move_right(row - 1, max(row - 3, -1), -1, piece.color, right_pos))
        if piece.color == Color.WHITE or piece.is_king():
            moves.update(self._move_left(row + 1, min(row + 3, self.board.rows), 1, piece.color, left_pos))
            moves.update(self._move_right(row + 1, min(row + 3, self.board.rows), 1, piece.color, right_pos))

        return moves

    def _move_left(self, start, stop, step, color, left_pos, skipped=None):
        if skipped is None:
            skipped = []

        moves = {}
        last = []
        for row in range(start, stop, step):
            if left_pos < 0:
                break

            current_piece = self.board.board[row][left_pos]
            if current_piece == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(row, left_pos)] = last + skipped
                else:
                    moves[(row, left_pos)] = last

                if last:
                    if step == -1:
                        row = max(row - 3, 0)
                    else:
                        row = min(row + 3, self.board.rows)
                    moves.update(self._move_left(row + step, row, step, color, left_pos - 1, skipped=last))
                    moves.update(self._move_right(row + step, row, step, color, left_pos + 1, skipped=last))
                break
            elif current_piece.color == color:
                break
            else:
                last = [current_piece]

            left_pos -= 1

        return moves

    def _move_right(self, start, stop, step, color, right, skipped=None):
        if skipped is None:
            skipped = []
        moves = {}
        last = []
        for row in range(start, stop, step):
            if right >= self.board.cols:
                break

            current = self.board.board[row][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(row, right)] = last + skipped
                else:
                    moves[(row, right)] = last

                if last:
                    if step == -1:
                        row = max(row - 3, 0)
                    else:
                        row = min(row + 3, self.board.rows)
                    moves.update(self._move_left(row + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._move_right(row + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
