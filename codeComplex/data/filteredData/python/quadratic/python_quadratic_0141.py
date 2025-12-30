from math import ceil
import random

mod = 10 ** 9 + 7


def get_original_pieces(x):
    common = (pow(x, 2) - 1) // 2
    first_piece = "10" * common + "1"
    second_piece = "0" + "10" * common
    return [first_piece, second_piece]


def solve_from_pieces(n, pieces):
    original_pieces = get_original_pieces(n)
    till = n * n

    fp = [[0, i] for i in range(4)]
    sp = [[0, i] for i in range(4)]

    for i in range(4):
        fpc, spc = 0, 0
        for j in range(till):
            if pieces[i][j] != original_pieces[0][j]:
                fpc += 1
            if pieces[i][j] != original_pieces[1][j]:
                spc += 1
        fp[i][0] = fpc
        sp[i][0] = spc

    fp.sort()
    sp.sort()

    ans1 = fp[0][0] + fp[1][0]
    ans2 = sp[0][0] + sp[1][0]

    for i in range(4):
        if sp[i][1] not in (fp[0][1], fp[1][1]):
            ans1 += sp[i][0]
        if fp[i][1] not in (sp[0][1], sp[1][1]):
            ans2 += fp[i][0]

    return min(ans1, ans2)


def generate_test_data(n, flip_prob=0.1):
    """
    根据 n 生成 4 个 n×n 的棋盘块（字符串形式，每块长度 n^2）。
    先构造目标棋盘，然后随机稍微扰动（翻转部分格子）。
    """
    target = [["0"] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 构造 2x2 块棋盘：使得右上和左下是一种模式，其余是另一种
            if (i // n + j // n) % 2 == 0:
                target[i][j] = "0" if (i + j) % 2 == 0 else "1"
            else:
                target[i][j] = "1" if (i + j) % 2 == 0 else "0"

    # 切成 4 个 n×n 块，这里直接复制同一个块用于测试
    pieces = []
    for _ in range(4):
        flat = []
        for i in range(n):
            for j in range(n):
                v = target[i][j]
                if random.random() < flip_prob:
                    v = "1" if v == "0" else "0"
                flat.append(v)
        pieces.append("".join(flat))
    return pieces


def main(n):
    """
    n: 棋盘规模（每块为 n×n，总为 2n×2n）。
    返回：最小需要翻转的格子数。
    """
    pieces = generate_test_data(n)
    return solve_from_pieces(n, pieces)


if __name__ == "__main__":
    # 示例运行：可自行修改 n
    n = 3
    print(main(n))