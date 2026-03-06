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
    # Interpret n as number of rows; choose m as bounded by log2(n+1) for scalability
    if n <= 0:
        return
    m = 1
    while (1 << m) <= n and m < 10:
        m += 1
    # ensure m at least 1
    if m < 1:
        m = 1
    # generate a deterministic n x m matrix a
    # a[i][j] = (i+1)*(j+2) % 1000 + (i//2 + j)
    a = [[(i + 1) * (j + 2) % 1000 + (i // 2 + j) for j in range(m)] for i in range(n)]

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
                    prev = mask ^ (1 << i)
                    if is_subset[mask] > is_subset[prev]:
                        is_subset[prev] = is_subset[mask]
        pos = False
        full_mask = (1 << m) - 1
        for mask in range(1 << m):
            if index[mask] == -1:
                continue
            mask2 = full_mask ^ mask
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

    res = solve(alpha)
    if res:
        print(res[0], res[1])
    else:
        print(-1, -1)


if __name__ == "__main__":
    main(10)