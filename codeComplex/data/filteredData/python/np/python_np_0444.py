def main(n):
    mod = int(1e9) + 7

    # Determine matrix dimensions from n
    # For scalability: let number of rows = n, number of columns = max(1, n//2)
    rows = n
    cols = max(1, n // 2)

    # Generate a deterministic matrix A of size rows x cols
    # Values are constructed deterministically using simple arithmetic
    A = [[(i * cols + j) % (10**9) for j in range(cols)] for i in range(rows)]

    def cal(x):
        l1 = set()
        d = {}
        for i in range(rows):
            k = 0
            for j in range(cols):
                if A[i][j] >= x:
                    k += 1 << j
            l1.add(k)
            d[k] = i + 1
        l1 = list(l1)
        s = (1 << cols) - 1
        a = []
        for i in l1:
            for j in l1:
                if i | j == s:
                    a = [d[i], d[j]]
        return a

    l, r = 0, 10**9
    last_mid = 0
    while l <= r:
        mid = (l + r) // 2
        last_mid = mid
        if cal(mid):
            l = mid + 1
        else:
            r = mid - 1
    a = cal(last_mid)
    if a:
        print(*a)
    else:
        print(*cal(last_mid - 1))


if __name__ == "__main__":
    main(10)