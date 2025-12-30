import random


def aburrimin(x, y, n, m, costder, costaba, dp):
    dists = []
    vals = []
    if x != 0:  # left
        dis = costder[y][x - 1]
        dists.append(dis)
        vals.append(dis + dp[y][x - 1])
    if y != 0:  # up
        dis = costaba[y - 1][x]
        dists.append(dis)
        vals.append(dis + dp[y - 1][x])
    if y < n - 1:  # down
        dis = costaba[y][x]
        dists.append(dis)
        vals.append(dis + dp[y + 1][x])
    if x < m - 1:  # right
        dis = costder[y][x]
        dists.append(dis)
        vals.append(dis + dp[y][x + 1])

    mindis = min(dists)
    return min(mindis + dp[y][x], min(vals))


def solvecaso(n, m, k, costder, costaba):
    if k % 2:
        for _ in range(n):
            print(" ".join("-1" for _ in range(m)))
        return

    k //= 2

    # double costs
    for ren in range(len(costder)):
        for col in range(len(costder[ren])):
            costder[ren][col] *= 2
    for ren in range(len(costaba)):
        for col in range(len(costaba[ren])):
            costaba[ren][col] *= 2

    dp = [[0 for _ in range(m)] for _ in range(n)]
    dptemp = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        for y in range(n):
            for x in range(m):
                dptemp[y][x] = aburrimin(x, y, n, m, costder, costaba, dp)
        dp, dptemp = dptemp, dp

    for ren in dp:
        print(" ".join(str(num) for num in ren))


def main(n):
    """
    n: 规模参数，用来生成测试数据。
       这里设定为一个 n×n 的网格，并令 k = 2*n 作为示例。
    """
    m = n
    k = 2 * n  # 可以根据需要调整 k 的生成方式

    # 生成测试数据：边权为 1~10 的随机整数
    random.seed(0)
    costder = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    costaba = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    solvecaso(n, m, k, costder, costaba)


if __name__ == "__main__":
    # 示例：以 n=4 运行
    main(4)