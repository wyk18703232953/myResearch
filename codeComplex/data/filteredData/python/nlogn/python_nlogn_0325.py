def main(n):
    # Generate a permutation a[1..n] deterministically.
    # We'll use a simple pattern: a[i] = (2*i) % n + 1, then fix collisions if needed.
    # But to keep logic clear and deterministic, we construct a permutation by rotation.
    if n <= 0:
        return
    a = [0] + [((i % n) + 1) for i in range(1, n + 1)]
    # Now a is [1,2,...,n] rotated by 0, but we want it not sorted for nontrivial behavior.
    # So rotate by 1 position for n > 1.
    if n > 1:
        a = [0] + a[2:] + a[1:2]

    d = {}
    for i in range(1, n + 1):
        d[a[i]] = i
    ans = 0
    for i in range(1, n + 1):
        if a[i] != i:
            ind1 = d[a[i]]
            ind2 = d[i]
            va1 = a[i]
            val2 = i
            a[ind1], a[ind2] = a[ind2], a[ind1]
            d[i] = i
            d[va1] = ind2
            ans += 1

    if (3 * n - ans) % 2 == 0:
        # print("Petr")
        pass

    else:
        # print("Um_nik")
        pass
if __name__ == "__main__":
    main(10)