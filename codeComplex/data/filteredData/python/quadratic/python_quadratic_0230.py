def main(n):
    # Deterministic data generation
    a = [i % (n // 2 + 1) + 1 for i in range(n)]
    cost = [(i * 3) % (n + 5) + 1 for i in range(n)]

    ans = float("inf")
    for i in range(n):
        m, r = float("inf"), float("inf")
        for j in range(i):
            if a[j] < a[i]:
                m = min(m, cost[j])
        for k in range(i + 1, n):
            if a[k] > a[i]:
                r = min(r, cost[k])
        ans = min(ans, cost[i] + m + r)
    # print(ans if ans != float("inf") else -1)
    pass
if __name__ == "__main__":
    main(10)