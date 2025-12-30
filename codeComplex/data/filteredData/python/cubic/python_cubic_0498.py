import random

def main(n):
    # 规模参数 n 控制 N、M、K，这里做一个简单映射：
    # N = M = max(1, n)，K 为偶数步长，至少为 2
    N = max(1, n)
    M = max(1, n)
    K = 2 * max(1, n // 2)  # 保证为偶数

    # 若 K 为奇数，按原逻辑输出 -1（但本构造中 K 一定是偶数）
    if K % 2:
        for _ in range(N):
            print(" ".join(["-1"] * M))
        return

    # 随机生成边权，范围可自行调整
    # colEdges: N 行，每行 M-1 条边权（左右相邻）
    colEdges = []
    for _ in range(N):
        # M-1 条水平边，对于 M=1 时为空列表
        edges = [random.randint(1, 10) for _ in range(max(0, M - 1))]
        colEdges.append(edges)

    # rowEdges: N-1 行，每行 M 条边权（上下相邻）
    rowEdges = []
    for _ in range(max(0, N - 1)):
        edges = [random.randint(1, 10) for _ in range(M)]
        rowEdges.append(edges)

    # 原逻辑：dp[k][i][j] 表示走 k*2 步的一半（即 k 次迭代，每次加 2 步）？
    # 这里保持原实现不改动，只是用生成的数据
    dp = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
    p = [[[(i, j) for j in range(M)] for i in range(N)] for _ in range(2)]
    prev = 0

    for _ in range(K // 2):
        cur = prev ^ 1
        for i in range(N):
            for j in range(M):
                cand = (float('inf'), None)

                if j:
                    nxt = (dp[prev][i][j - 1] + colEdges[i][j - 1], p[prev][i][j - 1])
                    cand = min(cand, nxt)
                if j < M - 1:
                    nxt = (dp[prev][i][j + 1] + colEdges[i][j], p[prev][i][j + 1])
                    cand = min(cand, nxt)
                if i:
                    nxt = (dp[prev][i - 1][j] + rowEdges[i - 1][j], p[prev][i - 1][j])
                    cand = min(cand, nxt)
                if i < N - 1:
                    nxt = (dp[prev][i + 1][j] + rowEdges[i][j], p[prev][i + 1][j])
                    cand = min(cand, nxt)

                dp[cur][i][j], p[cur][i][j] = cand
        prev = cur

    for i in range(N):
        for j in range(M):
            print(dp[prev][i][j] * 2, end=" ")
        print()


if __name__ == "__main__":
    # 示例：用 n=5 运行
    main(5)