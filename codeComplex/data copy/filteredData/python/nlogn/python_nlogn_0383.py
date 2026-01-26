def main(n):
    import heapq

    # Deterministic data generation based on n
    # n = length of arrays P and C
    k = n // 3  # choose k as a function of n, deterministic

    P = [(i * 7) % (n + 5) + 1 for i in range(n)]
    C = [(i * 11) % (n + 7) + 1 for i in range(n)]

    Q = []
    for i, p in enumerate(P):
        Q.append((p, i))
    Q.sort()

    q = []
    heapq.heapify(q)
    s = 0
    ans = [0] * n

    if k > 0:
        for p, i in Q:
            ans[i] = s + C[i]
            if len(q) == k:
                if q[0] <= C[i]:
                    v = heapq.heappop(q)
                    heapq.heappush(q, C[i])
                    s -= v
                    s += C[i]

            else:
                heapq.heappush(q, C[i])
                s += C[i]

    else:
        for p, i in Q:
            ans[i] = C[i]

    # print(*ans)
    pass
if __name__ == "__main__":
    main(10)