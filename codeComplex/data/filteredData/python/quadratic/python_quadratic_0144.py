def nSquaresToRecolorIn(brokenPieces, nSquares, squares):
    possible_nSquares = [
        (
            sum(1 for i in range(nSquares) if piece[i] != squares[:-1][i]),
            sum(1 for i in range(nSquares) if piece[i] != squares[1:][i]),
        )
        for piece in brokenPieces
    ]
    possible_nSquares.sort(key=lambda x: x[0])
    return possible_nSquares[0][0] + possible_nSquares[1][0] + possible_nSquares[2][1] + possible_nSquares[3][1]


def main(n):
    # n is the pieces_Dimension
    pieces_Dimension = n
    nSquares = pieces_Dimension * pieces_Dimension

    # Deterministically generate four pieces, each of length nSquares
    # Pattern uses only arithmetic on indices, no randomness
    piece1 = ''.join('01'[(i + 0) % 2] for i in range(nSquares))
    piece2 = ''.join('01'[(i + 1) % 2] for i in range(nSquares))
    piece3 = ''.join('01'[(i // pieces_Dimension) % 2] for i in range(nSquares))
    piece4 = ''.join('01'[(i // pieces_Dimension + i % pieces_Dimension) % 2] for i in range(nSquares))

    brokenPieces = (piece1, piece2, piece3, piece4)
    squares = '01' * (-(-nSquares // 2))

    return nSquaresToRecolorIn(brokenPieces, nSquares, squares)


if __name__ == "__main__":
    # Example deterministic call for timing/complexity experiments
    # print(main(10))
    pass