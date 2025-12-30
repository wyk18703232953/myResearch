import sys
import random

def transform(c):
    if c == '.':
        return 0
    if c == '#':
        return 1
    return 2

def take_care(board, n, m, N, M):
    if n + 2 >= N:
        return
    if m + 2 >= M:
        return
    if (board[n][m+1] == 0 or board[n][m+2] == 0 or
        board[n+1][m] == 0 or board[n+1][m+2] == 0 or
        board[n+2][m] == 0 or board[n+2][m+1] == 0 or
        board[n+2][m+2] == 0):
        return
    board[n][m] = 2
    board[n][m+1] = 2
    board[n][m+2] = 2
    board[n+1][m] = 2
    board[n+1][m+2] = 2
    board[n+2][m] = 2
    board[n+2][m+1] = 2
    board[n+2][m+2] = 2
    return False, board

def generate_board(N, M):
    # 随机生成由 '.' 和 '#' 组成的棋盘
    # 可以根据需要调整密度，这里设置 '#' 概率约为 50%
    board_chars = []
    for _ in range(N):
        row = []
        for _ in range(M):
            row.append('#' if random.random() < 0.5 else '.')
        board_chars.append(row)
    # 转换为数值棋盘
    board = [[transform(c) for c in row] for row in board_chars]
    return board

def main(n):
    # 将规模 n 映射为一个 N x M 的棋盘，这里简单设为 N = M = n
    N = n
    M = n
    if N <= 0 or M <= 0:
        print("YES")
        return

    board = generate_board(N, M)

    for i in range(N):
        for j in range(M):
            take_care(board, i, j, N, M)

    for row in board:
        if 1 in row:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    # 示例：当直接运行脚本时，以 n = 5 为规模
    main(5)