def main(n):
    # 生成测试数据：4 个 n×n 的 0/1 棋盘，每个棋盘随机生成
    import random

    boards = []
    for _ in range(4):
        board = []
        for _ in range(n):
            row = ''.join(str(random.randint(0, 1)) for _ in range(n))
            board.append(row)
        boards.append(board)

    # 按照原逻辑计算每个棋盘的 df
    s = []
    for i in range(4):
        df = 0
        for k in range(n):
            l = boards[i][k]
            for j in range(n):
                if int(l[j]) == (k + j) % 2:
                    df += 1
        s.append(df)

    ans = min(
        s[0] + s[1] + n * n - s[2] + n * n - s[3],
        s[0] + s[2] + n * n - s[1] + n * n - s[3],
        s[0] + s[3] + n * n - s[1] + n * n - s[2],
        s[1] + s[2] + n * n - s[0] + n * n - s[3],
        s[1] + s[3] + n * n - s[0] + n * n - s[2],
        s[2] + s[3] + n * n - s[0] + n * n - s[1],
    )

    print(ans)
    return ans


if __name__ == '__main__':
    # 示例：n = 3 运行一次
    main(3)