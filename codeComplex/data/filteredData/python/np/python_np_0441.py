def main(n):
    import math as mt

    # Map n to matrix dimensions:
    # n is the number of rows, m is the number of columns.
    # Ensure m >= 1.
    m = max(1, n // 2 + 1)

    # Deterministically generate matrix a of size n x m
    # Values constructed by simple arithmetic so they grow with n, m.
    a = [[(i * m + j) % (10 ** 6) for j in range(m)] for i in range(n)]

    ans = []
    lo = 0
    hi = 10 ** 9

    def vanguda(mid: int) -> bool:
        nonlocal ans
        f = {}
        for i in range(n):
            bi = 0
            for j in range(m):
                if a[i][j] >= mid:
                    bi += 1
                bi <<= 1
            f[bi >> 1] = i
        full_mask = (1 << m) - 1
        for aa, bb in f.items():
            for cc, dd in f.items():
                if aa | cc == full_mask:
                    ans = (bb + 1, dd + 1)
                    return True
        return False

    while lo <= hi:
        mid = (lo + hi) // 2
        if vanguda(mid):
            lo = mid + 1
        else:
            hi = mid - 1

    # For time-complexity experiments, we still return or print something
    # deterministic based on the core logic.
    if ans:
        print(ans[0], ans[1])
    else:
        print(-1, -1)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments.
    main(10)