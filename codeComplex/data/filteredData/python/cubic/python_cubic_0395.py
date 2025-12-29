import random

def main(n):
    # 生成测试数据：n 行 m 列的网格，k 为偶数
    m = n                    # 这里令列数等于行数，可按需调整
    k = 2 * max(1, n // 2)   # 生成一个与规模相关的偶数步数 k >= 2

    # 生成 A: n x m 水平方向边权（每行有 m-1 条边，但原代码使用 m 元素行）
    # 为保持结构一致，这里仍生成 n x m，每个值范围 1..9
    A = [[random.randint(1, 9) for _ in range(m)] for _ in range(n)]

    # 生成 B: (n-1) x m 垂直方向边权
    B = [[random.randint(1, 9) for _ in range(m)] for _ in range(max(0, n - 1))]

    # 原逻辑开始
    if k % 2 == 0:
        O = [[[10**12] * m for _ in range(n)] for _ in range(k // 2)]
        # l = 0 初始化：一步走出去再回来，取最近边的代价
        for i in range(n):
            for j in range(m):
                if i > 0:
                    O[0][i][j] = min(O[0][i][j], B[i - 1][j])
                if i < n - 1:
                    O[0][i][j] = min(O[0][i][j], B[i][j])
                if j > 0:
                    O[0][i][j] = min(O[0][i][j], A[i][j - 1])
                if j < m - 1:
                    O[0][i][j] = min(O[0][i][j], A[i][j])

        # 逐步扩展到 k/2 步的一侧路径
        for l in range(1, k // 2):
            for i in range(n):
                for j in range(m):
                    cur = O[l][i][j]
                    if i > 0:
                        val = B[i - 1][j] + O[l - 1][i - 1][j]
                        if val < cur:
                            cur = val
                    if i < n - 1:
                        val = B[i][j] + O[l - 1][i + 1][j]
                        if val < cur:
                            cur = val
                    if j > 0:
                        val = A[i][j - 1] + O[l - 1][i][j - 1]
                        if val < cur:
                            cur = val
                    if j < m - 1:
                        val = A[i][j] + O[l - 1][i][j + 1]
                        if val < cur:
                            cur = val
                    O[l][i][j] = cur

        # 输出结果：往返路径长度是单侧 * 2
        for i in range(n):
            print(*[O[-1][i][j] * 2 for j in range(m)])
    else:
        # k 为奇数时，不可能返回原点
        for _ in range(n):
            print(*([-1] * m))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)