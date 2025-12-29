def main(n):
    import random

    INF = 1 << 60

    # 这里将规模 n 映射为 N, M, K，可按需要调整
    N = max(1, n)
    M = max(1, n)
    # 让 K 为偶数以产生有效结果，如需测试奇数情况可修改
    K = 2 * max(1, n // 2)

    # 生成测试数据：
    # e1: N 行，每行 M-1 个权值（左右相邻边）
    # e2: N-1 行，每行 M 个权值（上下相邻边）
    # 使用 1~9 的小正整数方便观察
    e1 = [
        [random.randint(1, 9) for _ in range(M - 1)]
        for _ in range(N)
    ]
    e2 = [
        [random.randint(1, 9) for _ in range(M)]
        for _ in range(N - 1)
    ]

    def new_dp():
        return [[INF] * M for _ in range(N)]

    def solve():
        if K % 2 == 1:
            for _ in range(N):
                print(*([-1] * M))
            return

        dp_prev = [[0] * M for _ in range(N)]

        for _ in range(K // 2):
            dp_cur = new_dp()
            # 左右移动
            for row in range(N):
                for col in range(M - 1):
                    cost = e1[row][col]
                    # 从 (row, col+1) 到 (row, col)
                    dp_cur[row][col] = min(dp_cur[row][col],
                                           dp_prev[row][col + 1] + cost)
                    # 从 (row, col) 到 (row, col+1)
                    dp_cur[row][col + 1] = min(dp_cur[row][col + 1],
                                               dp_prev[row][col] + cost)

            # 上下移动
            for row in range(N - 1):
                for col in range(M):
                    cost = e2[row][col]
                    # 从 (row+1, col) 到 (row, col)
                    dp_cur[row][col] = min(dp_cur[row][col],
                                           dp_prev[row + 1][col] + cost)
                    # 从 (row, col) 到 (row+1, col)
                    dp_cur[row + 1][col] = min(dp_cur[row + 1][col],
                                               dp_prev[row][col] + cost)

            dp_prev = dp_cur

        for row in range(N):
            res_row = [2 * x for x in dp_prev[row]]
            print(*res_row)

    solve()


if __name__ == '__main__':
    # 示例：以 n=5 运行
    main(5)