import random


def solve(start, n, delta, delta2):
    inf = 2 * 10**9
    dp = [[-1] * n for _ in range(1 << n)]
    dp[1 << start][start] = inf
    stack = [(1 << start, start)]

    for _ in range(1, n + 1):
        next_stack = []
        for bitmask, v in stack:
            for dest in range(n):
                if (1 << dest) & bitmask:
                    continue
                new_mask = bitmask | (1 << dest)
                if dp[new_mask][dest] == -1:
                    next_stack.append((new_mask, dest))
                dp[new_mask][dest] = max(
                    dp[new_mask][dest],
                    min(dp[bitmask][v], delta[v][dest])
                )
        stack = next_stack

    full_mask = (1 << n) - 1
    best = 0
    for j in range(n):
        if j == start:
            continue
        best = max(best, min(delta2[j][start], dp[full_mask][j]))
    return best


def main(n):
    # 生成测试数据：n 行，每行 m 列
    # 这里令 m = max(2, n) 保证至少 2 列
    m = max(2, n)

    # 为了避免所有差值为 0，使用一定范围内的随机整数
    # 你也可以根据需要修改生成规则
    random.seed(0)
    matrix = [
        [random.randint(0, 1000) for _ in range(m)]
        for _ in range(n)
    ]

    if n == 1:
        ans = min(abs(x - y) for x, y in zip(matrix[0], matrix[0][1:]))
        print(ans)
        return

    # 预计算 delta: 行与行之间对应列差值的最小值
    delta = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            delta_ij = min(abs(x - y) for x, y in zip(matrix[i], matrix[j]))
            delta[i][j] = delta_ij
            delta[j][i] = delta_ij

    # 预计算 delta2: 行 i 与行 j 的“右移一位”对齐后差值的最小值
    inf = 2 * 10**9
    delta2 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # matrix[j][1:] 与 matrix[i] 对齐
            # 可能为空序列，所以提供 default
            delta2[i][j] = min(
                (abs(x - y) for x, y in zip(matrix[i], matrix[j][1:])),
                default=inf
            )

    result = 0
    for i in range(n):
        result = max(result, solve(i, n, delta, delta2))

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(4)
    main(4)