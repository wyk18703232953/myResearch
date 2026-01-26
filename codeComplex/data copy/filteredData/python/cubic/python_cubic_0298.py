import sys
sys.setrecursionlimit(200000)


def solve(r, g, b, R, G, B, z):
    if (r == 0 and g == 0) and (r == 0 and b == 0) and (g == 0 and b == 0):
        return 0
    if z[r][g][b] != -1:
        return z[r][g][b]

    d = e = f = 0
    if r != 0 and g != 0:
        d = R[r - 1] * G[g - 1] + solve(r - 1, g - 1, b, R, G, B, z)
    if r != 0 and b != 0:
        e = R[r - 1] * B[b - 1] + solve(r - 1, g, b - 1, R, G, B, z)
    if b != 0 and g != 0:
        f = B[b - 1] * G[g - 1] + solve(r, g - 1, b - 1, R, G, B, z)

    z[r][g][b] = max(d, e, f)
    return z[r][g][b]


def main(n: int):
    """
    n 为规模参数，这里用作每种颜色数量的上限。
    测试数据生成策略：
    - r, g, b ∈ [1, n]（若 n=0，则直接输出 0）
    - R, G, B 各为 1..r/g/b 的升序整数列表，作为示例数据
    """
    if n <= 0:
        # print(0)
        pass
        return

    # 简单的数据生成方式：让 r=g=b=n
    r = g = b = n

    # 生成一些有序的正整数作为颜色值
    # 例如：R = [1,2,...,r], G = [2,4,...,2g], B = [3,6,...,3b]
    R = list(range(1, r + 1))
    G = [2 * i for i in range(1, g + 1)]
    B = [3 * i for i in range(1, b + 1)]

    # 原算法中本来就会进行排序，此处保持一致
    R.sort()
    G.sort()
    B.sort()

    # 初始化记忆化数组
    z = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    ans = solve(r, g, b, R, G, B, z)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：以 n = 3 运行
    main(3)