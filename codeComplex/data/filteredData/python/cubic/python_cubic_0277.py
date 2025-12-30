import random

# 全局变量声明
r = g = b = None
rl = bl = gl = None
dp = None

def rec(i, j, k):
    if (i == rl and j == bl) or (i == rl and k == gl) or (k == gl and j == bl):
        return 0
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    else:
        x = r[i] * b[j]
        y = b[j] * g[k]
        z = r[i] * g[k]
        if x > 0:
            x += rec(i + 1, j + 1, k)
        if y > 0:
            y += rec(i, j + 1, k + 1)
        if z > 0:
            z += rec(i + 1, j, k + 1)

        dp[i][j][k] = max(x, y, z)
        return dp[i][j][k]

def main(n):
    """
    n 为规模参数，用于生成测试数据。
    这里将三种颜色数组长度都设为 n（可根据需要调整比例）。
    数组元素为 1..100 的随机正整数。
    """
    global r, g, b, rl, bl, gl, dp

    # 生成测试数据
    rl = bl = gl = n
    r = [random.randint(1, 100) for _ in range(rl)] + [0]
    b = [random.randint(1, 100) for _ in range(bl)] + [0]
    g = [random.randint(1, 100) for _ in range(gl)] + [0]

    # DP 数组初始化
    dp = [[[-1 for _ in range(gl + 1)] for _ in range(bl + 1)] for _ in range(rl + 1)]

    # 排序（与原逻辑一致）
    r.sort(reverse=True)
    b.sort(reverse=True)
    g.sort(reverse=True)

    i = j = k = 0
    ans = rec(i, j, k)
    print(ans)


# 示例：需要时可调用 main(n)，如：
# main(3)