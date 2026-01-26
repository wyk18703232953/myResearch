def main(n):
    if n <= 0:
        pieces_dimension = 1

    else:
        pieces_dimension = n

    n_squares = pieces_dimension * pieces_dimension

    base_pattern = ''.join('1' if (i + j) % 2 == 0 else '0'
                           for i in range(pieces_dimension)
                           for j in range(pieces_dimension))

    piece1 = base_pattern
    piece2 = base_pattern[::-1]
    piece3_list = list(base_pattern)
    for i in range(0, len(piece3_list), 3):
        piece3_list[i] = '1' if piece3_list[i] == '0' else '0'
    piece3 = ''.join(piece3_list)
    piece4 = ''.join('1' if c == '0' else '0' for c in base_pattern)

    broken_pieces = (piece1, piece2, piece3, piece4)

    squares = '01' * (n_squares // 2) + ('0' if n_squares % 2 == 1 else '')

    return n_squares_to_recolor_in(broken_pieces, n_squares, squares)


def n_squares_to_recolor_in(brokenPieces, nSquares, squares):
    possible_nSquares = [sum(piece[i] != squares[i] for i in range(nSquares)) for piece in brokenPieces]
    possible_nSquares.sort()
    return 2 * nSquares + possible_nSquares[0] + possible_nSquares[1] - possible_nSquares[2] - possible_nSquares[3]


if __name__ == "__main__":
    result = main(5)
    # print(result)
    pass