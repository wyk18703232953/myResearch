import random

def main(n):
    # 生成规模
    # n: 行数
    # 为了可复现，设定一些规则
    m = n                         # 列数，简化为正方形网格
    k = 2 * random.randint(1, n)  # 生成一个偶数步数（至少2）

    # 生成测试数据：right 和 down 的权值
    # 权值范围可以根据需求调整
    max_w = 10
    right = [[random.randint(1, max_w) for _ in range(m)] for _ in range(n)]
    down = [[random.randint(1, max_w) for _ in range(m)] for _ in range(n - 1)]

    # 如果 k 为奇数，则按照原逻辑输出 -1 矩阵
    if k & 1:
        for _ in range(n):
            print(*([-1] * m))
        return

    # 初始化 DP 数组
    half_k = k // 2
    INF = float('inf')
    mem = [[[INF] * (half_k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

    # 初始化步数为 0 时的代价为 0
    for i in range(n):
        for j in range(m):
            mem[i][j][0] = 0

    # 动态规划
    for k1 in range(1, half_k + 1):
        for i in range(n):
            for j in range(m):
                ans = []
                # 向上
                if i - 1 >= 0:
                    ans.append(mem[i - 1][j][k1 - 1] + down[i - 1][j])
                else:
                    ans.append(INF)
                # 向下
                if i + 1 < n:
                    ans.append(mem[i + 1][j][k1 - 1] + down[i][j])
                else:
                    ans.append(INF)
                # 向左
                if j - 1 >= 0:
                    ans.append(mem[i][j - 1][k1 - 1] + right[i][j - 1])
                else:
                    ans.append(INF)
                # 向右
                if j + 1 < m:
                    ans.append(mem[i][j + 1][k1 - 1] + right[i][j])
                else:
                    ans.append(INF)

                mem[i][j][k1] = min(ans)

    # 输出结果（往返路径代价乘 2）
    for i in range(n):
        print(*[mem[i][x][half_k] * 2 for x in range(m)])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)