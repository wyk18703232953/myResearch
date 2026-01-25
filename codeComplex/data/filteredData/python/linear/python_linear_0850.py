def main(n):
    # Ensure n is at least 1
    if n <= 0:
        return

    # Deterministically generate a permutation of [1..n]
    # Using a simple arithmetic-based shuffle that is reversible and deterministic
    a = [(i * 3) % n + 1 for i in range(n)]

    rev = [-1] * (n + 1)
    for i, j in enumerate(a):
        rev[j] = i

    mx = max(a)

    l = a.index(mx)
    r = l

    for i in range(n - 1, 0, -1):
        idx = rev[i]
        if idx == l - 1:
            l -= 1
        elif idx == r + 1:
            r += 1
        else:
            print('NO')
            return
    print('YES')


if __name__ == "__main__":
    # Example: run main with a specific n for experiment
    main(10)