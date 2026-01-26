def nSquaresToRecolorIn(brokenPieces, nSquares, squares):
    possible_nSquares = [
        (
            sum(1 for i in range(nSquares) if piece[i] != squares[:-1][i]),
            sum(1 for i in range(nSquares) if piece[i] != squares[1:][i]),
        )
        for piece in brokenPieces
    ]
    possible_nSquares.sort(key=lambda x: x[0])
    return (
        possible_nSquares[0][0]
        + possible_nSquares[1][0]
        + possible_nSquares[2][1]
        + possible_nSquares[3][1]
    )


def main(n):
    if n <= 0:
        return 0

    pieces_Dimension = n
    nSquares = pieces_Dimension * pieces_Dimension
    squares = "01" * (-(-nSquares // 2))

    # Deterministic generation of 4 pieces, each of size n x n, flattened
    piece1 = "".join("1" if (i + j) % 2 == 0 else "0" for i in range(n) for j in range(n))
    piece2 = "".join("1" if (i + j) % 2 == 1 else "0" for i in range(n) for j in range(n))
    piece3 = "".join("1" if (i * j) % 3 == 0 else "0" for i in range(n) for j in range(n))
    piece4 = "".join("1" if (i * j) % 3 != 0 else "0" for i in range(n) for j in range(n))

    brokenPieces = (piece1, piece2, piece3, piece4)

    return nSquaresToRecolorIn(brokenPieces, nSquares, squares)


if __name__ == "__main__":
    # print(main(5))
    pass