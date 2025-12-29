# 将原始逻辑封装到 main(n) 中
# n 作为规模参数，用于生成测试数据（r,g,b 以及对应数组的长度不超过 n）

def solve(x, y, z):
    global r, g, b, ra, ga, ba, ans, memo
    if (x > r - 1 and y > g - 1) or (x > r - 1 and z > b - 1) or (y > g - 1 and z > b - 1):
        return 0
    if memo[x][y][z] != -1:
        return memo[x][y][z]

    mx = 0
    if x < r and y < g:
        mx = max(mx, ra[x] * ga[y] + solve(x + 1, y + 1, z))
    if x < r and z < b:
        mx = max(mx, ra[x] * ba[z] + solve(x + 1, y, z + 1))
    if y < g and z < b:
        mx = max(mx, ga[y] * ba[z] + solve(x, y + 1, z + 1))

    ans = max(ans, mx)
    memo[x][y][z] = mx
    return mx


def main(n):
    """
    n 为规模参数。
    这里根据 n 生成测试数据：
    - r, g, b 为不超过 n 的正整数
    - ra, ga, ba 为长度分别为 r, g, b 的非负整数数组（可按需修改生成策略）
    """

    import random

    global r, g, b, ra, ga, ba, ans, memo

    # 生成 r, g, b （至少为 1，最多为 n，且不超过原代码中 memo 的设计规模 205）
    limit = min(n, 200)  # 防止超过 memo 固定大小
    r = random.randint(1, limit)
    g = random.randint(1, limit)
    b = random.randint(1, limit)

    # 生成数组数据（0~9 的随机整数，可根据需要调整）
    ra = sorted([random.randint(0, 9) for _ in range(r)], reverse=True)
    ga = sorted([random.randint(0, 9) for _ in range(g)], reverse=True)
    ba = sorted([random.randint(0, 9) for _ in range(b)], reverse=True)

    # 初始化 memo 与 ans
    memo = [[[-1 for _ in range(205)] for _ in range(205)] for _ in range(205)]
    ans = 0

    solve(0, 0, 0)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)