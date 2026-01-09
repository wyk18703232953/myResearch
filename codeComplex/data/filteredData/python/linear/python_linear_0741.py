def count(audrey, imba, banget):
    return (imba - audrey - 1) % (banget - 1)

def main(n):
    # Map n to problem parameters:
    # n: size of array L
    # q: number of queries
    if n < 2:
        n = 2
    N = n
    Q = n

    # Deterministically construct array L of length N
    # Example pattern: L[i] = (i * 3) % (2*N) + 1  (all positive, varied)
    L = [((i * 3) % (2 * N)) + 1 for i in range(N)]

    maxi = max(L)
    indexmax = L.index(maxi)
    P = []
    # Simulate original process to fill P and get Y
    for _ in range(indexmax):
        P.append((L[0], L[1]))
        if L[0] < L[1]:
            L.append(L.pop(0))

        else:
            L.append(L.pop(1))
    Y = tuple(L[1:])

    # Deterministically construct queries m (1-based)
    # Cover small and large ranges relative to indexmax
    queries = []
    for i in range(Q):
        if i % 3 == 0:
            m = (i % (indexmax + 1)) + 1  # ensures some m <= indexmax

        else:
            m = indexmax + 1 + (i % max(1, (N - 1)))  # ensures some m > indexmax
        queries.append(m)

    # Process queries and print results (same format as original)
    for m in queries:
        if m <= indexmax:
            # print(str(P[m - 1][0]) + " " + str(P[m - 1][1]))
            pass

        else:
            # print(str(maxi) + " " + str(Y[count(indexmax, m, N)]))
            pass
if __name__ == "__main__":
    main(10)