def main(n):
    # Interpret n as the length of the arrays s and c
    if n < 3:
        # print(-1)
        pass
        return

    # Deterministic generation of s and c
    # s: a pattern with some ups and downs to allow possible valid triplets
    # c: simple increasing costs
    s = [(i * 2 + (i % 3)) for i in range(n)]
    # introduce some decreases to allow s[i] < s[mid] < s[k]
    for i in range(1, n, 5):
        s[i] = s[i - 1] - 1
    c = [i % 7 + 1 for i in range(n)]

    maxx = float('inf')
    ans = maxx

    for mid in range(1, n - 1):
        l = [maxx] + [c[i] for i in range(mid) if s[i] < s[mid]]
        r = [maxx] + [c[i] for i in range(mid + 1, n) if s[i] > s[mid]]
        ans = min(ans, min(l) + c[mid] + min(r))

    # print(ans if ans != float('inf') else -1)
    pass
if __name__ == "__main__":
    main(10)