def main(n):
    # n controls:
    # - number of elements in V (before adding 10**9)
    # - number of candidate triples m (we set m = n for scalable experiments)

    if n <= 0:
        # print(0)
        pass
        return

    m = n

    # Deterministically generate V of length n
    # Example pattern: V[i] = 2 * i + 1 (strictly increasing positive integers)
    V = [2 * i + 1 for i in range(n)]
    V.sort()
    V.append(10 ** 9)
    n_plus = n + 1  # this is original n after increment

    # Deterministically generate m triples (x1, x2, y)
    # We only care about triples with x1 == 1 and their x2 values.
    # Pattern:
    #   x1 alternates between 1 and 2
    #   x2 grows linearly with i
    #   y is any deterministic function, here y = i
    X2 = []
    for i in range(m):
        x1 = 1 if i % 2 == 0 else 2
        x2 = i * 3 + 2
        y = i
        if x1 == 1:
            X2.append(x2)

    X2.sort()
    k = len(X2)
    i = 0
    j = 0
    ans = 10 ** 9 + 7
    c = 0

    # Core algorithm unchanged
    while i < n_plus:
        while j < k:
            if X2[j] < V[i]:
                c += 1
                j += 1

            else:
                break
        ans = min(ans, k - c + i)
        i += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)