def main(n):
    # Map n to sizes of the two sequences
    m = n
    # Deterministic data generation
    seq = [i % (n // 2 + 1) for i in range(n)]
    f = [i % (m // 3 + 1) for i in range(m)]

    a = []
    for i in range(n):
        for j in range(m):
            if seq[i] == f[j]:
                a.append(seq[i])

    for i in range(len(a)):
        # print(a[i], end=' ')
        pass
    # print()
    pass
if __name__ == "__main__":
    main(10)