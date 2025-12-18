# _
#####################################################################################################################

def main():
    pieces_Dimension = int(input())
    piece1 = ''.join(input() for _ in range(pieces_Dimension))
    input()
    piece2 = ''.join(input() for _ in range(pieces_Dimension))
    input()
    piece3 = ''.join(input() for _ in range(pieces_Dimension))
    input()
    piece4 = ''.join(input() for _ in range(pieces_Dimension))

    brokenPieces = (piece1, piece2, piece3, piece4)
    nSquares = pieces_Dimension*pieces_Dimension
    squares = '01'*(nSquares//2) + '0'

    return nSquaresToRecolorIn(brokenPieces, nSquares, squares)


def nSquaresToRecolorIn(brokenPieces, nSquares, squares):
    possible_nSquares = [sum(piece[i] != squares[i] for i in range(nSquares)) for piece in brokenPieces]
    possible_nSquares.sort()

    return 2*nSquares + possible_nSquares[0] + possible_nSquares[1] - possible_nSquares[2] - possible_nSquares[3]


if __name__ == '__main__':
    print(main())
    # main()
