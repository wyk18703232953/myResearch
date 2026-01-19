import math as mt

def main(n):
    # Map n to matrix dimensions
    # For scalability and square-ish matrices, use:
    # rows = n, cols = max(1, n // 2)
    rows = n
    cols = max(1, n // 2)

    # Deterministic matrix generation based only on n, i, j
    # a[i][j] grows moderately with i, j so binary search has work to do
    a = [[(i + 1) * (j + 2) + (i ^ j) for j in range(cols)] for i in range(rows)]

    ans = []
    lo = 0
    hi = 10**9

    def vanguda(mid: int) -> bool:
        nonlocal ans
        f = {}
        for i in range(rows):
            bi = 0
            for j in range(cols):
                if a[i][j] >= mid:
                    bi += 1
                bi <<= 1
            f[bi >> 1] = i
        full_mask = (1 << cols) - 1
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

    if ans:
        print(ans[0], ans[1])
    else:
        print(-1, -1)


if __name__ == "__main__":
    main(10)