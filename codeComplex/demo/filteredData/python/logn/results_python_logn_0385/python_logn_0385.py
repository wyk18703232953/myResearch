def main(n):
    if n % 4 == 2:
        return -1

    # Deterministic hidden function for simulation of interactive judge.
    # It must be periodic with period n and satisfy f(i + n//2) = something useful.
    # We construct it based on a fixed pivot p = n//3 (deterministic).
    p = n // 3

    # Build f as 1D array of size n+1 (1-based index).
    # For 1 <= i <= n:
    #   f[i] = (i <= p) ? 0 : 1
    # Then f(i + n//2) is defined for i in [1, n//2].
    f = [0] * (n + 1)
    for i in range(1, n + 1):
        f[i] = 0 if i <= p else 1

    memo = [-1] * (n + 1)

    def check(i):
        if memo[i] == -1:
            # Simulate interactive query
            idx = ((i - 1) % n) + 1
            memo[i] = f[idx]
        return memo[i]

    l = 1
    r = l + n // 2

    while r >= l:
        a = check(l)
        b = check(l + n // 2)

        if a == b:
            return l

        mid = (l + r) >> 1

        c = check(mid)
        d = check(mid + n // 2)

        if c == d:
            return mid

        if (a < b and c < d) or (a > b and c > d):
            l = mid + 1

        else:
            r = mid

    return -1


if __name__ == "__main__":
    # Example deterministic call for timing experiments
    # Adjust n as needed when running experiments
    result = main(100000)
    # print(result)
    pass