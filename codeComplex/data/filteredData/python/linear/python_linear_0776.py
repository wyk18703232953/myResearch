def main(n):
    # Interpret n as the number of elements in L
    # Deterministically construct n, m, k, and L based on n
    # Keep constraints simple but non-trivial:
    # Let k be a small positive integer depending on n
    k = max(1, n // 5)
    m = n * 3

    # Generate a non-decreasing sequence L of length n within [1, m]
    # Use a simple arithmetic pattern to ensure determinism
    L = [1 + (i * 3) % m for i in range(n)]
    L.sort()

    off = 1
    page = -1
    c = 0
    ans = 0
    for l in L:
        p = (l - off) // k
        if p == page:
            c += 1
        else:
            off += c
            c = 1
            ans += 1
            page = (l - off) // k

    print(ans)


if __name__ == "__main__":
    main(10)