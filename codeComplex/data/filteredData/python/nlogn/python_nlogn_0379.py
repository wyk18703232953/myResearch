import heapq

def main(n):
    # Interpret n as the size of arrays P and C, and let k be a function of n
    if n <= 0:
        return
    k = max(1, n // 2)

    # Deterministic generation of P and C
    P = [(i * 3 + 1) % (2 * n + 1) for i in range(n)]
    C = [(i * 5 + 2) % (3 * n + 1) for i in range(n)]

    X = []
    for i in range(n):
        X.append([P[i], C[i], i])
    X.sort(key=lambda x: x[0])

    coins = []
    heapq.heapify(coins)
    curr = 0
    res = [0 for _ in range(n)]

    limit = min(k, n)
    for i in range(limit):
        heapq.heappush(coins, X[i][1])
        curr += X[i][1]
        res[X[i][2]] = curr

    for j in range(limit, n):
        res[X[j][2]] = X[j][1] + sum(coins)
        if len(coins) > 0:
            x = heapq.heappop(coins)
            if x < X[j][1]:
                heapq.heappush(coins, X[j][1])
            else:
                heapq.heappush(coins, x)

    print(*res)


if __name__ == "__main__":
    main(10)