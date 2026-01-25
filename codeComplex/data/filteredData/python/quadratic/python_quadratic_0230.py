def main(n):
    # Generate deterministic input data based on n
    # a: strictly increasing sequence to ensure many valid triplets
    # cost: some deterministic pattern depending on index
    a = list(range(1, n + 1))
    cost = [(i * 3 + 1) % 100 + 1 for i in range(n)]

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
    return ans if ans != float("inf") else -1


if __name__ == "__main__":
    # Example call for time-complexity experiments
    result = main(10)
    print(result)