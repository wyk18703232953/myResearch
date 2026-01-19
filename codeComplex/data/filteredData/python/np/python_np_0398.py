from math import ceil, inf

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

def run_once(n, m, a):
    alpha, omega = 0, 10**9

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
                    is_subset[mask ^ (1 << i)] = max(is_subset[mask], is_subset[mask ^ (1 << i)])
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
    if n <= 0:
        return
    m = max(1, n // 5)
    max_m = 10
    if m > max_m:
        m = max_m
    n_rows = n
    base = 10 ** 6
    mod_val = 10 ** 9 + 7
    a = []
    for i in range(n_rows):
        row = []
        for j in range(m):
            val = (i * (m + 3) + j * 7 + base) % mod_val
            row.append(val)
        a.append(row)
    res = run_once(n_rows, m, a)
    if res:
        print(res[0], res[1])
    else:
        print(-1, -1)

if __name__ == "__main__":
    main(10)