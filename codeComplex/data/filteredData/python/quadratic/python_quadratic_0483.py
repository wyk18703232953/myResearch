def main(n):
    # Ensure n is at least 1 to avoid invalid indexing
    if n <= 0:
        return

    # Deterministically generate l and r based on n.
    # We generate l and r so that they are consistent with some k,
    # mimicking a valid input case for the original algorithm.

    # First, create a deterministic k sequence of length n
    # Example: k[i] = (i * 2) % (n + 3) + (i // 2)
    k = [(i * 2) % (n + 3) + (i // 2) for i in range(n)]

    # Compute l and r from k in the same way the original program does
    l = []
    r = []
    for i in range(n):
        c = 0
        d = 0
        for j in range(0, i):
            if k[j] > k[i]:
                c += 1
        for j in range(i + 1, n):
            if k[j] > k[i]:
                d += 1
        l.append(c)
        r.append(d)

    # Now apply the original logic using the generated l and r

    # Original pre-checks
    if l[0] != 0 or r[n - 1] != 0:
        print("NO")
        return

    s = [l[i] + r[i] for i in range(n)]
    m = max(s) + 1
    k_reconstructed = []
    for i in s:
        k_reconstructed.append(m - i)

    l1 = []
    r1 = []
    for i in range(n):
        c = 0
        d = 0
        for j in range(0, i):
            if k_reconstructed[j] > k_reconstructed[i]:
                c += 1
        l1.append(c)
        for j in range(i + 1, n):
            if k_reconstructed[j] > k_reconstructed[i]:
                d += 1
        r1.append(d)

    if l1 != l or r1 != r:
        print("NO")
    else:
        print("YES")
        print(*k_reconstructed)


if __name__ == "__main__":
    # Example deterministic calls for time complexity experiments
    # You can change or loop these n values as needed.
    for size in [1, 5, 10, 50]:
        print(f"n = {size}")
        main(size)