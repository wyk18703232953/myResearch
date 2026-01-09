def main(n):
    # Deterministic generation of parameters based on n
    # Interpret n as the length of array a
    # Define m and k as simple deterministic functions of n
    if n <= 0:
        n = 1
    m = max(1, n // 5)
    k = 3

    # Deterministic generation of array a of length n
    # Example pattern: a[i] = (i % 7) - 3
    a = [(i % 7) - 3 for i in range(n)]

    def max_sum(a):
        nonlocal m, k
        if len(a) == 0:
            return 0
        elif len(a) == 1:
            return max(0, a[0] - k)
        mid = len(a) // 2
        l_rec = max_sum(a[:mid])
        r_rec = max_sum(a[mid:])
        l_bests = [0] * m
        r_bests = [0] * m
        l_sum = 0
        for idx in range(1, mid + 1):
            l_sum += a[mid - idx]
            if idx % m == 0:
                l_sum -= k
            l_bests[idx % m] = max(l_bests[idx % m], l_sum)
        r_sum = 0
        for idx in range(0, len(a) - mid):
            r_sum += a[idx + mid]
            if (idx + 1) % m == 0:
                r_sum -= k
            r_bests[(idx + 1) % m] = max(r_bests[(idx + 1) % m], r_sum)

        best_acr = 0
        for i in range(m):
            for j in range(m):
                best_acr = max(
                    best_acr,
                    l_bests[i]
                    + r_bests[j]
                    - (k if i + j > 0 else 0)
                    - (k if i + j > m else 0),
                )
        ans = max(l_rec, r_rec, best_acr)
        return ans

    ans = max_sum(a)
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)