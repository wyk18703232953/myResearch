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
    if n <= 0:
        return 0

    pieces_Dimension = n
    nSquares = pieces_Dimension * pieces_Dimension
    squares = "01" * (-(-nSquares // 2))

    # Deterministic generation of 4 pieces, each of length n*n
    # pattern: piece index and position index decide '0' or '1'
    brokenPieces = []
    for p in range(4):
        piece_chars = [
            "01"[(i + p) % 2] for i in range(nSquares)
        ]
        brokenPieces.append("".join(piece_chars))
    brokenPieces = tuple(brokenPieces)

    return nSquaresToRecolorIn(brokenPieces, nSquares, squares)


if __name__ == "__main__":
    # Example deterministic call; change n as needed for experiments
    print(main(5))