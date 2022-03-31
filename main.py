from game import Game

if __name__ == '__main__':
    game = Game()

    game.draw()

    piece = game.board.get_piece(0, 2)

    game.move(piece=piece, row=3, col=1)

    game.draw()
