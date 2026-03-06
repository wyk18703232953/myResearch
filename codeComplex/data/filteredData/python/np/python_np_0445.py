def main(n):
    # Map n to matrix size: n rows, m columns with m = max(1, n//2)
    m = max(1, n // 2)

    # Deterministic matrix generation: a[i][j] = (i + 1) * (j + 2)
    a = [[(i + 1) * (j + 2) for j in range(m)] for i in range(n)]

    ans = (-1, -1)

    def solve(x: int) -> bool:
        nonlocal ans
        dp = {}
        full_mask = (1 << m) - 1
        for i in range(n):
            temp = 0
            for j in range(m):
                if a[i][j] >= x:
                    temp |= (1 << j)
            dp[temp] = i
        for aa, bb in dp.items():
            for cc, dd in dp.items():
                if aa | cc == full_mask:
                    ans = (bb + 1, dd + 1)
                    return True
        return False

    l, r = 0, 10 ** 9
    while l <= r:
        mid = (l + r) // 2
        if solve(mid):
            l = mid + 1
        else:
            r = mid - 1
    print(*ans)


if __name__ == "__main__":
    main(10)