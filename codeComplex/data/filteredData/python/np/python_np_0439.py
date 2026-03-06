def main(n):
    mod = 998244353
    INF = float('inf')

    # Interpret n as both number of rows and columns for scalability
    # Ensure at least 1x1 matrix
    if n <= 0:
        n = 1
    m = n

    # Deterministic matrix generation:
    # arr[i][j] = (i * 131 + j * 197 + 7) % 1000000000
    arr = [[(i * 131 + j * 197 + 7) % 1000000000 for j in range(m)] for i in range(n)]

    res = []

    def c(num):
        nonlocal res
        dic = {}
        for i in range(n):
            now = 0
            for j in range(m):
                if arr[i][j] >= num:
                    now |= 1 << j
            dic[now] = i + 1

        full_mask = (1 << m) - 1
        for k, v in dic.items():
            for kk, vv in dic.items():
                if k | kk == full_mask:
                    res = (v, vv)
                    return True

        return False

    l, r = 0, 10**9
    while l <= r:
        mp = (l + r + 1) // 2
        now = c(mp)
        if now:
            l = mp + 1
        else:
            r = mp - 1

    print(*res)


if __name__ == "__main__":
    main(10)