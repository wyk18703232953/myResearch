import random

def main(n):
    # 随机生成测试数据规模：
    # n 行, m 列, k 为偶数步数
    m = max(1, n)                      # 设 m 与 n 同级别
    # 生成一个合理的偶数 k，与 n,m 同级别
    k = max(2, 2 * (n // 2))           # 保证 k 为偶数且 >= 2

    # 生成权值矩阵：right 权值为 n×m, down 权值为 (n-1)×m
    # 权值范围可以自行调整
    MAX_W = 10**3
    right = [[random.randint(1, MAX_W) for _ in range(m)] for _ in range(n)]
    down = [[random.randint(1, MAX_W) for _ in range(m)] for _ in range(n - 1)]

    if k & 1:
        # k 为奇数时，无解，输出 -1
        for _ in range(n):
            print(*([-1] * m))
        return

    # DP 数组：mem[i][j][t] 表示从 (i,j) 出发走 t 步的最小代价
    half_k = k // 2
    INF = float('inf')
    mem = [[[INF] * (half_k + 1) for _ in range(m)] for _ in range(n)]

    # 边界：走 0 步代价为 0
    for i in range(n):
        for j in range(m):
            mem[i][j][0] = 0

    # 辅助函数：判断 (x,y) 是否在网格内
    def valid(x, y):
        return 0 <= x < n and 0 <= y < m

    # 逐步扩展步数
    for t in range(1, half_k + 1):
        for i in range(n):
            for j in range(m):
                best = INF

                # 上
                if valid(i - 1, j):
                    cost = mem[i - 1][j][t - 1] + down[i - 1][j]
                    if cost < best:
                        best = cost
                # 下
                if valid(i + 1, j):
                    cost = mem[i + 1][j][t - 1] + down[i][j]
                    if cost < best:
                        best = cost
                # 左
                if valid(i, j - 1):
                    cost = mem[i][j - 1][t - 1] + right[i][j - 1]
                    if cost < best:
                        best = cost
                # 右
                if valid(i, j + 1):
                    cost = mem[i][j + 1][t - 1] + right[i][j]
                    if cost < best:
                        best = cost

                mem[i][j][t] = best

    # 输出从每个点出发走恰好 k 步的最小代价（往返，所以 *2）
    for i in range(n):
        row_ans = [mem[i][j][half_k] * 2 for j in range(m)]
        print(*row_ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)