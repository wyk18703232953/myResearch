def main(n):
    import bisect

    if n < 3:
        # print(-1)
        pass
        return

    # Deterministically generate s and c based on n
    s = [(i * 2 + 1) % (n + 7) for i in range(n)]
    c = [(i * 3 + 5) % (n + 11) + 1 for i in range(n)]

    INF = 10 ** 18
    ans = INF
    for mid in range(1, n - 1):
        l1 = [c[i] for i in range(mid) if s[i] < s[mid]] + [INF]
        l2 = [c[i] for i in range(mid + 1, n) if s[i] > s[mid]] + [INF]
        ans = min(ans, min(l1) + c[mid] + min(l2))
    if ans >= INF:
        # print(-1)
        pass

    else:
        # print(ans)
        pass
if __name__ == "__main__":
    main(10)