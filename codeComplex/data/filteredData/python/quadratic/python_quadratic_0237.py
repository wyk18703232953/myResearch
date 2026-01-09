def main(n):
    # Generate deterministic test data based on n
    # s: strictly increasing sequence 1..n
    s = list(range(1, n + 1))
    # c: some deterministic cost pattern depending on i
    c = [(i * 3) % 7 + (i // 2) for i in range(n)]

    INF = 10 ** 18
    ans = INF
    if n >= 3:
        for mid in range(1, n - 1):
            l1 = [c[i] for i in range(mid) if s[i] < s[mid]] + [INF]
            l2 = [c[i] for i in range(mid + 1, n) if s[i] > s[mid]] + [INF]
            val = min(l1) + c[mid] + min(l2)
            if val < ans:
                ans = val
    if ans >= INF:
        # print(-1)
        pass

    else:
        # print(ans)
        pass
if __name__ == "__main__":
    # Example call; adjust n for scaling experiments
    main(10)