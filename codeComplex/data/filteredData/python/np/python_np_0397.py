from math import inf
import random


def prod(a, mod=10 ** 9 + 7):
    ans = 1
    for each in a:
        ans = (ans * each) % mod
    return ans


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(a, b):
    return a * b // gcd(a, b)


def binary(x, length=16):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y


def main(n):
    # 依据规模 n 生成测试数据：
    # 原程序中有 n, m 以及 n x m 的矩阵 a
    # 这里约定：
    #   m = min(10, max(1, n.bit_length()))，保证位运算规模适中
    #   a[i][j] 在 [0, 10^9] 中随机生成
    if n <= 0:
        return

    m = min(10, max(1, n.bit_length()))
    max_val = 10 ** 9

    # 生成矩阵 a (n x m)
    rng = random.Random(0)
    a = [[rng.randint(0, max_val) for _ in range(m)] for _ in range(n)]

    alpha, omega = 0, max_val

    def solve(mid):
        index = [-1] * (1 << m)
        for i in range(n):
            val = 0
            for j in range(m):
                if a[i][j] >= mid:
                    val += (1 << j)
            index[val] = i + 1
        pos = False
        full = (1 << m) - 1
        for mask in range(1 << m):
            if index[mask] == -1:
                continue
            for mask2 in range(1 << m):
                if mask | mask2 != full:
                    continue
                if index[mask2] != -1:
                    pos = (index[mask], index[mask2])
                    return pos
        return pos

    while alpha < omega:
        mid = (alpha + omega + 1) // 2
        if solve(mid):
            alpha = mid
        else:
            omega = mid - 1

    ans = solve(alpha)
    if ans:
        print(*ans)
    else:
        # 若无解，按照原逻辑不会发生，但这里做个兜底
        print(-1, -1)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)