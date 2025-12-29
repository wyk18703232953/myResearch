import random

def main(n):
    # n: pieces_Dimension, also the side length of each piece

    pieces_Dimension = n
    nSquares = pieces_Dimension * pieces_Dimension

    # generate a target chessboard pattern of size n*n
    squares = ('01' * (nSquares // 2) + '0')[:nSquares]

    # generate 4 random pieces, each as a length-nSquares string of '0'/'1'
    def random_piece():
        return ''.join(random.choice('01') for _ in range(nSquares))

    piece1 = random_piece()
    piece2 = random_piece()
    piece3 = random_piece()
    piece4 = random_piece()

    brokenPieces = (piece1, piece2, piece3, piece4)

    return nSquaresToRecolorIn(brokenPieces, nSquares, squares)


def nSquaresToRecolorIn(brokenPieces, nSquares, squares):
    possible_nSquares = [
        sum(piece[i] != squares[i] for i in range(nSquares))
        for piece in brokenPieces
    ]
    possible_nSquares.sort()
    return 2 * nSquares + possible_nSquares[0] + possible_nSquares[1] - possible_nSquares[2] - possible_nSquares[3]