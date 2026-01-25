def main(n):
    # Generate a deterministic parent array p for a tree of size n
    # p[1] is unused, p[2..n] are parents
    if n <= 0:
        return

    p = [0, 0]
    for i in range(2, n + 1):
        # Deterministic parent choice: connect node i to i//2 (always < i)
        p.append(i // 2)

    d = [0] * (n + 1)

    for i in range(n, 1, -1):
        if d[i] == 0:
            d[i] = 1
        d[p[i]] += d[i]

    if n == 1:
        d[1] = 1

    d = d[1:]
    d.sort()

    print(*d)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)