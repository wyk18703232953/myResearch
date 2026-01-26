def main(n):
    mod = 998244353

    def sod(x):
        s = 0
        while x:
            s += x % 10
            x //= 10
        return s

    # Deterministic generation of n,s based on input scale n
    # Original problem has two integers: n and s
    big_n = n
    s = max(0, n // 2)

    def fun(mid):
        return mid - sod(mid) >= s

    l = 0
    r = big_n
    ans = -1
    while l <= r:
        m = l + (r - l) // 2
        if fun(m):
            ans = m
            r = m - 1

        else:
            l = m + 1
    if ans == -1:
        ans = big_n + 1
    result = big_n - ans + 1
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10_000_000)