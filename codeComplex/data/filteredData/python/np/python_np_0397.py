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


from math import inf


def run_algorithm(n, m, a):
    alpha, omega = 0, 10 ** 9

    def solve(mid):
        index = [-1] * (1 << m)
        for i in range(n):
            val = 0
            for j in range(m):
                if a[i][j] >= mid:
                    val += (1 << j)
            index[val] = i + 1
        pos = False
        full_mask = (1 << m) - 1
        for mask in range(1 << m):
            if index[mask] == -1 and mask != full_mask:
                continue
            for mask2 in range(1 << m):
                if mask | mask2 != full_mask:
                    continue
                if min(index[mask], index[mask2]) != -1:
                    pos = (index[mask], index[mask2])
                    return pos
        return pos

    while alpha < omega:
        mid = (alpha + omega + 1) // 2
        if solve(mid):
            alpha = mid
        else:
            omega = mid - 1
    return solve(alpha)


def main(n):
    # Map n to problem size:
    # n rows, m columns (fixed small so that 2^m is manageable)
    # Ensure m >= 1
    m = 8
    if n <= 0:
        n = 1

    # Deterministic matrix generation:
    # a[i][j] = (i * (j + 1) + j * j + 7) % 1000000000
    a = [[(i * (j + 1) + j * j + 7) % (10 ** 9) for j in range(m)] for i in range(n)]

    res = run_algorithm(n, m, a)
    # Single print as in original
    print(res[0], res[1])


if __name__ == "__main__":
    # Example deterministic call for timing/experiments
    main(1000)