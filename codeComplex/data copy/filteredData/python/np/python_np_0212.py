def main(n):
    # Define deterministic parameters based on n
    l = n
    r = 2 * n
    x = max(1, n // 10)

    # Deterministically generate C as a list of n integers
    C = [i % 10 + 1 for i in range(1, n + 1)]

    k = 0
    limit = 1 << n
    for i in range(limit):
        W = [w for w, b in zip(C, bin(i)[2:].zfill(n)) if b == '1']
        if not W:
            continue
        s = sum(W)
        if l <= s <= r and max(W) - min(W) >= x:
            k += 1
    print(k)


if __name__ == "__main__":
    main(10)