def main(n):
    # n controls size of the initial array and number of queries
    if n <= 0:
        return

    # Deterministically generate array d of length n
    # Example pattern: d[i] = (i * 2 + 3) % (n + 5)
    d = [(i * 2 + 3) % (n + 5) for i in range(n)]

    odd = 0
    for i in range(n):
        for j in range(i, n):
            if d[i] > d[j]:
                odd ^= 1

    # Let m be proportional to n for scaling; here we choose m = n
    m = n
    ans = []

    # Deterministically generate m queries (l, r) within [0, n-1]
    # Pattern ensures 0 <= l <= r < n
    for i in range(m):
        l = i % n
        r = (i * 3 + 1) % n
        if l > r:
            l, r = r, l
        k = r - l + 1
        if ((k * (k - 1) // 2) % 2):
            odd ^= 1
        ans.append("odd" if odd else "even")

    # print("\n".join(ans))
    pass
if __name__ == "__main__":
    main(10)