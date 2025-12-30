import random

def main(n):
    # n: pieces_Dimension (size of each piece is n x n)
    pieces_Dimension = n
    nSquares = pieces_Dimension * pieces_Dimension
    squares = '01' * (-(-nSquares // 2))

    # 根据 n 生成测试数据：生成4个 n x n 的随机01字符块
    def gen_piece():
        return ''.join(random.choice('01') for _ in range(nSquares))

    piece1 = gen_piece()
    piece2 = gen_piece()
    piece3 = gen_piece()
    piece4 = gen_piece()

    brokenPieces = (piece1, piece2, piece3, piece4)

    return nSquaresToRecolorIn(brokenPieces, nSquares, squares)


def nSquaresToRecolorIn(brokenPieces, nSquares, squares):
    possible_nSquares = [
        (
            sum(1 for i in range(nSquares) if piece[i] != squares[:-1][i]),
            sum(1 for i in range(nSquares) if piece[i] != squares[1:][i])
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


if __name__ == '__main__':
    # 示例调用：n=4
    print(main(4))