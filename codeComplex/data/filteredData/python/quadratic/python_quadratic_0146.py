def nSquaresToRecolorIn(brokenPieces, nSquares, squares):
    possible_nSquares = [sum(piece[i] != squares[i] for i in range(nSquares)) for piece in brokenPieces]
    possible_nSquares.sort()
    return 2 * nSquares + possible_nSquares[0] + possible_nSquares[1] - possible_nSquares[2] - possible_nSquares[3]


def main(n):
    if n <= 0:
        return 0

    pieces_Dimension = n
    nSquares = pieces_Dimension * pieces_Dimension

    # Deterministic generation of 4 pieces, each as a concatenation of n strings of length n
    piece1 = ''.join(''.join('1' if (i + j) % 2 == 0 else '0' for j in range(pieces_Dimension)) for i in range(pieces_Dimension))
    piece2 = ''.join(''.join('0' if (i + j) % 3 == 0 else '1' for j in range(pieces_Dimension)) for i in range(pieces_Dimension))
    piece3 = ''.join(''.join('1' if (i * j) % 4 == 0 else '0' for j in range(pieces_Dimension)) for i in range(pieces_Dimension))
    piece4 = ''.join(''.join('0' if (i * i + j) % 5 == 0 else '1' for j in range(pieces_Dimension)) for i in range(pieces_Dimension))

    brokenPieces = (piece1, piece2, piece3, piece4)

    squares = '01' * (nSquares // 2) + ('0' if nSquares % 2 == 1 else '')

    return nSquaresToRecolorIn(brokenPieces, nSquares, squares)


if __name__ == "__main__":
    # print(main(5))
    pass