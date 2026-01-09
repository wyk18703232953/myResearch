def main(n):
    # n controls the size of the initial array and the number of queries
    if n <= 0:
        return

    # Deterministic construction of the initial array of length n
    values = [(i * 2 + 1) % (n + 3) for i in range(n)]

    cnt = 0
    # Count initial inversions exactly as in the original logic
    for i in range(n):
        for j in range(i + 1, n):
            if values[i] > values[j]:
                cnt += 1

    # Deterministic construction of m and of the queries
    m = n
    results = []
    for i in range(m):
        # Deterministic query generation: ensure 0 <= l <= r < n
        l = i % n
        r = (i * 3 + 1) % n
        if l > r:
            l, r = r, l
        length = r - l + 1

        cnt += length * (length - 1) // 2
        cnt &= 1

        if cnt == 1:
            results.append("odd")

        else:
            results.append("even")

    # Output results
    for line in results:
        # print(line)
        pass
if __name__ == "__main__":
    main(5)