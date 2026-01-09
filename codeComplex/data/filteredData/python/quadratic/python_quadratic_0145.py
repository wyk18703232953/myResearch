def nSquaresToRecolorIn(brokenPieces, nSquares, squares):
    possible_nSquares = [
        (
            sum(piece[i] != squares[:-1][i] for i in range(nSquares)),
            sum(piece[i] != squares[1:][i] for i in range(nSquares)),
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
    pieces_Dimension = max(1, n)
    nSquares = pieces_Dimension * pieces_Dimension

    piece1 = "".join("01"[(i + j) % 2] for i in range(pieces_Dimension) for j in range(pieces_Dimension))
    piece2 = "".join("01"[(i * 2 + j) % 2] for i in range(pieces_Dimension) for j in range(pieces_Dimension))
    piece3 = "".join("01"[(i + j * 2) % 2] for i in range(pieces_Dimension) for j in range(pieces_Dimension))
    piece4 = "".join("01"[(i + j + 1) % 2] for i in range(pieces_Dimension) for j in range(pieces_Dimension))

    brokenPieces = (piece1, piece2, piece3, piece4)
    squares = "01" * (-(-nSquares // 2))

    return nSquaresToRecolorIn(brokenPieces, nSquares, squares)


if __name__ == "__main__":
    # print(main(5))
    pass