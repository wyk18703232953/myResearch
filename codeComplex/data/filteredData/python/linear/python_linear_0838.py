def main(n):
    D = {"R": 0, "G": 1, "B": 2}

    # Deterministically generate Q queries based on n
    Q = max(1, n)
    queries = []
    for t in range(Q):
        # Generate N and K deterministically from t and n
        N = max(1, n + t % (n + 1))
        K = max(1, (t % N) + 1)

        # Generate string S of length N deterministically
        chars = ["R", "G", "B"]
        S = "".join(chars[(i + t) % 3] for i in range(N))
        queries.append((N, K, S))

    results = []
    for N, K, S in queries:
        mi = K
        for i in range(3):
            d = 0
            for j in range(N):
                if D[S[j]] != (i + j) % 3:
                    d += 1
                if j >= K and D[S[j - K]] != (i + j - K) % 3:
                    d -= 1
                if j >= K - 1:
                    if d < mi:
                        mi = d
        results.append(mi)

    # To keep the side effect similar to the original program
    for x in results:
        # print(x)
        pass
if __name__ == "__main__":
    main(10)