def main(n):
    # Interpret n as:
    # n = number of rows
    # m = number of columns
    # Values in matrix are deterministic based on i, j, and n
    if n <= 0:
        return

    m = max(1, n // 2)

    # Build matrix l deterministically
    # Example: l[i][j] = (i * 131 + j * 137 + n) % 1000000000
    l = [[(i * 131 + j * 137 + n) % 1000000000 for j in range(m)] for i in range(n)]

    from collections import defaultdict

    pm = (1 << m) - 1

    def find(x):
        s = set()
        d = defaultdict(int)
        for i in range(n):
            bits = 0
            for j in range(m):
                if l[i][j] >= x:
                    bits |= (1 << j)
            d[bits] = i
            s.add(bits)
        s = list(s)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if (s[i] | s[j]) == pm:
                    return [d[s[i]] + 1, d[s[j]] + 1]
        return [-1, -1]

    st = 0
    end = 10 ** 9
    ans = (0, 0)
    while st <= end:
        mid = (st + end) // 2
        res = find(mid)
        if res[0] != -1:
            ans = res
            st = mid + 1
        else:
            end = mid - 1

    print(ans[0], ans[1])


if __name__ == "__main__":
    main(10)