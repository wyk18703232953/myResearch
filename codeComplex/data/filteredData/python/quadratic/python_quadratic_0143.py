import itertools
import random


def check_board(corner, board, n):
    ans = 0
    cur = corner
    for i in range(n):
        for j in range(n):
            if board[i][j] != cur:
                ans += 1
            cur = 1 - cur
        # 每行换行时，棋盘颜色也要翻转一次
        cur = 1 - cur
    return ans


def solve(corner, p, boards, n):
    ans = check_board(corner, boards[p[0]], n)
    ans += check_board(1 - corner, boards[p[1]], n)
    ans += check_board(1 - corner, boards[p[2]], n)
    ans += check_board(corner, boards[p[3]], n)
    return ans


def main(n):
    # 生成测试数据：4 个 n×n 的 0/1 棋盘
    boards = []
    for _ in range(4):
        board = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
        boards.append(board)

    ans = n * n * 4
    for p in itertools.permutations(range(4), 4):
        ans = min(ans, solve(1, p, boards, n))
        ans = min(ans, solve(0, p, boards, n))

    print(ans)


if __name__ == "__main__":
    # 示例：可以修改 n 测试
    main(4)