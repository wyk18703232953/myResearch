import random

def main(n):
    # 生成规模为 n 的测试数据
    pieces_Dimension = n
    nSquares = pieces_Dimension * pieces_Dimension

    # 构造目标棋盘模式（与原逻辑一致）
    squares = '01' * (-(-nSquares // 2))

    # 随机生成 4 个碎片，每个碎片为长度 nSquares 的 0/1 字符串
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