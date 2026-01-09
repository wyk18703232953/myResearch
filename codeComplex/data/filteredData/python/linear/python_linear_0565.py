def main(n):
    # Generate a deterministic parent array p[2..n]
    # Ensure p[i] < i to form a valid rooted tree with root at 1
    p = [0, 0]
    for i in range(2, n + 1):
        p.append((i - 1) // 2 + 1 if i > 2 else 1)

    d = [0] * (n + 1)

    for i in range(n, 1, -1):
        if d[i] == 0:
            d[i] = 1
        d[p[i]] += d[i]

    if n == 1:
        d[1] = 1

    d = d[1:]
    d.sort()
    # print(*d)
    pass
if __name__ == "__main__":
    main(10)