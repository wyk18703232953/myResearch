def main(n):
    # Interpret n as matrix size: n rows, n columns
    rows = n
    cols = n

    # Deterministically generate matrix a of size rows x cols
    # Values are constructed via simple arithmetic to be deterministic.
    a = [[(i * cols + j) % (10**9) for j in range(cols)] for i in range(rows)]

    ans = []

    def check(mid: int) -> bool:
        nonlocal ans
        dic = {}
        for i in range(rows):
            bit = 0
            for j in range(cols):
                if a[i][j] >= mid:
                    bit += 1
                bit <<= 1
            dic[bit >> 1] = i
        for x, idx in dic.items():
            for y, idy in dic.items():
                if x | y == 2**cols - 1:
                    ans = (idx + 1, idy + 1)
                    return True
        return False

    le = 0
    ri = int(1e9)
    while le <= ri:
        mid = (le + ri) >> 1
        if check(mid):
            le = mid + 1
        else:
            ri = mid - 1

    if ans:
        print(ans[0], ans[1])
    else:
        print(-1, -1)


if __name__ == "__main__":
    main(5)