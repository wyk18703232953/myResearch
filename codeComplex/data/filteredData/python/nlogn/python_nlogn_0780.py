def main(n):
    # Interpret n as the number of elements N; set K deterministically as N//2 + 1 (at least 1)
    N = max(1, n)
    K = max(1, N // 2 + 1)

    # Deterministic generation of array a of length N
    # Example pattern: a[i] = (i * 3 + i // 2) to create varying differences
    a = [(i * 3 + i // 2) for i in range(N)]

    # Core logic from original program
    diff = []
    for i in range(1, N):
        diff.append([i, a[i] - a[i - 1]])
    diff = sorted(diff, key=lambda x: -x[1])
    res = max(a) - min(a)
    k = 0
    while k < K - 1 and k < len(diff):
        res -= diff[k][1]
        k += 1
    print(res)


if __name__ == "__main__":
    main(10)