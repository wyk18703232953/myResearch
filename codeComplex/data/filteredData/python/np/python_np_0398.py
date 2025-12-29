from math import inf
import random

MOD = 10 ** 9 + 7


def prod(a, mod=MOD):
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


def solve_instance(a, n, m):
    alpha, omega = 0, 10 ** 9

    def solve(mid):
        index = [-1] * (1 << m)
        for i in range(n):
            val = 0
            for j in range(m):
                if a[i][j] >= mid:
                    val += (1 << j)
            index[val] = i + 1
        is_subset = list(index)
        for i in range(m):
            for mask in range(1 << m):
                if mask & (1 << i):
                    is_subset[mask ^ (1 << i)] = max(
                        is_subset[mask], is_subset[mask ^ (1 << i)]
                    )
        pos = False
        for mask in range(1 << m):
            if index[mask] == -1:
                continue
            mask2 = ((1 << m) - 1) ^ mask
            if is_subset[mask2] != -1:
                pos = (index[mask], is_subset[mask2])
                break
        return pos

    while alpha < omega:
        mid = (alpha + omega + 1) // 2
        if solve(mid):
            alpha = mid
        else:
            omega = mid - 1
    return solve(alpha)


def main(n):
    # 依据规模 n 生成测试数据：
    # 这里令矩阵为 n 行、m 列，其中 m = min( max(1, n.bit_length()), 10 )
    # 元素为 [0, 1e9] 内的随机整数
    random.seed(0)
    m = min(max(1, n.bit_length()), 10)
    a = [[random.randint(0, 10 ** 9) for _ in range(m)] for _ in range(n)]

    i1, i2 = solve_instance(a, n, m)
    print(i1, i2)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)