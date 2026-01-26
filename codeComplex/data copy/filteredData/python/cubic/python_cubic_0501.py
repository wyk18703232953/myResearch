def main(n):
    INF = 1 << 60
    MOD = 10 ** 9 + 7

    # 映射 n 到 N, M, K，使规模随 n 线性增长
    if n < 1:
        n = 1
    N = max(1, n)
    M = max(1, (n % 10) + 1)  # 防止 M 过小或为 0
    # 让 K 随 n 增长，并保证既有偶数也有奇数情况可测
    K = 2 * (n % 5)  # 0,2,4,6,8 中的一种，可调整为奇数测试时再改

    # 确保可以测试到偶数/奇数情况，这里固定为偶数，便于运行 DP
    if K == 0:
        K = 2

    # 生成确定性权值矩阵 e1 (N x (M-1)) 和 e2 ((N-1) x M)
    # 使用简单算术规则生成
    e1 = []
    for i in range(N):
        row = []
        for j in range(M - 1):
            # 保证正成本，随 i, j 有变化
            val = (i + 1) * (j + 2)
            row.append(val)
        e1.append(row)

    e2 = []
    for i in range(N - 1):
        row = []
        for j in range(M):
            val = (i + 2) * (j + 1)
            row.append(val)
        e2.append(row)

    def new_dp():
        return [[INF] * M for _ in range(N)]

    if K % 2 == 1:
        # 输出与原程序行为一致
        for _ in range(N):
            # print(*([-1] * M))
            pass
        return

    dp_prev = [[0] * M for _ in range(N)]

    for _ in range(K // 2):
        dp_cur = new_dp()
        for row in range(N):
            for col in range(M - 1):
                cost = e1[row][col]
                if dp_prev[row][col + 1] + cost < dp_cur[row][col]:
                    dp_cur[row][col] = dp_prev[row][col + 1] + cost
                if dp_prev[row][col] + cost < dp_cur[row][col + 1]:
                    dp_cur[row][col + 1] = dp_prev[row][col] + cost
        for row in range(N - 1):
            for col in range(M):
                cost = e2[row][col]
                if dp_prev[row + 1][col] + cost < dp_cur[row][col]:
                    dp_cur[row][col] = dp_prev[row + 1][col] + cost
                if dp_prev[row][col] + cost < dp_cur[row + 1][col]:
                    dp_cur[row + 1][col] = dp_prev[row][col] + cost
        dp_prev = dp_cur

    for row in range(N):
        res_row = [2 * x for x in dp_prev[row]]
        # print(*res_row)
        pass
if __name__ == "__main__":
    # 示例：以 n = 10 作为输入规模
    main(10)