def main(n):
    # Interpret n as the number of test cases Q.
    Q = n if n > 0 else 1

    results = []

    for t in range(Q):
        # Deterministically define N and K for each test case based on t.
        # Ensure N >= 1 and K in [1, N]
        N = 5 + (t * 7)  # linear growth with t
        K = 1 + (t * 3) % N

        # Deterministically construct S of length N using a simple pattern.
        # Colors cycle through "RGB" based on index and test index.
        base = "RGB"
        S = "".join(base[(i + t) % 3] for i in range(N))

        X = [{"R": 0, "G": 1, "B": 2}[s] for s in S]
        mi = K
        for i in range(3):
            d = 0
            for j in range(N):
                if X[j] != (i + j) % 3:
                    d += 1
                if j >= K and X[j - K] != (i + j - K) % 3:
                    d -= 1
                if j >= K - 1:
                    mi = min(mi, d)
        results.append(mi)

    for v in results:
        print(v)


if __name__ == "__main__":
    main(3)