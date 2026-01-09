def main(n):
    # 生成规模为 n 的测试数据：2 行 n 列的棋盘
    # 这里使用全 '.' 的棋盘，可按需要修改成其他生成规则
    board = [list("." * n) for _ in range(2)]

    figures = [
        ((0, 0), (0, 1), (1, 0)),
        ((0, 0), (0, 1), (1, 1)),
        ((0, 1), (1, 0), (1, 1)),
        ((0, 0), (1, 0), (1, 1)),
    ]

    ans = 0
    for j in range(n - 1):
        for fig in figures:
            ok = 1
            for fi, fj in fig:
                if board[fi][j + fj] == 'X':
                    ok = 0
                    break
            if not ok:
                continue
            ans += 1
            for fi, fj in fig:
                board[fi][j + fj] = 'X'

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)