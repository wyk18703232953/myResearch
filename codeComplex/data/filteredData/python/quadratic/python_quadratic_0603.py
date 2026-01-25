def main(n):
    # n controls the input size: length of array a
    if n <= 0:
        n = 1
    # Deterministic generation of parameters
    m = max(1, n // 3)
    k = n // 2 + 1
    # Deterministic array a of length n
    a = [((i * 7) % 17) - 8 for i in range(n)]

    def max_sum(a, n, m, k):
        if n == 0:
            return 0
        if n == 1:
            return max(0, a[0] - k)

        mid = n // 2
        l_rec = max_sum(a[:mid], mid, m, k)
        r_rec = max_sum(a[mid:], n - mid, m, k)

        l_bests = [0] * m
        r_bests = [0] * m

        # best sums ending at mid-1 going leftwards
        l_sum = 0
        for idx in range(1, mid + 1):
            l_sum += a[mid - idx]
            if idx % m == 0:
                l_sum -= k
            r = idx % m
            if l_sum > l_bests[r]:
                l_bests[r] = l_sum

        # best sums starting at mid going rightwards
        r_sum = 0
        for idx in range(0, n - mid):
            r_sum += a[mid + idx]
            if (idx + 1) % m == 0:
                r_sum -= k
            r = (idx + 1) % m
            if r_sum > r_bests[r]:
                r_bests[r] = r_sum

        best_acr = 0
        for i in range(m):
            for j in range(m):
                val = l_bests[i] + r_bests[j]
                if i + j > 0:
                    val -= k
                if i + j > m:
                    val -= k
                if val > best_acr:
                    best_acr = val

        if l_rec >= r_rec and l_rec >= best_acr:
            return l_rec
        if r_rec >= l_rec and r_rec >= best_acr:
            return r_rec
        return best_acr

    ans = max_sum(a, n, m, k)
    print(ans)


if __name__ == "__main__":
    main(10)