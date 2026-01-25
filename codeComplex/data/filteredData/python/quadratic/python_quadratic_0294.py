def main(n):
    # n is the number of pairs; total length of a is 2*n
    if n <= 0:
        print(0)
        return

    # Deterministic construction:
    # Make pairs (1,1), (2,2), ..., (n,n) and then shift the second half by 1 position cyclically
    a = []
    for i in range(1, n + 1):
        a.extend([i, i])
    if n > 1:
        b = a[:]
        # rotate the second element of each pair cyclically
        for i in range(n):
            # position of the second element in pair i
            idx = 2 * i + 1
            # take element from the next pair's second position (cyclic)
            src_idx = (2 * ((i + 1) % n) + 1)
            b[idx] = a[src_idx]
        a = b

    swaps = 0
    for i in range(0, 2 * n, 2):
        if a[i] == a[i + 1]:
            continue

        c = a[i]
        j = i + 2
        while j < 2 * n and c != a[j]:
            j += 1

        MIN = i + 1
        while j > MIN:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
            swaps += 1

    print(swaps)


if __name__ == "__main__":
    main(5)