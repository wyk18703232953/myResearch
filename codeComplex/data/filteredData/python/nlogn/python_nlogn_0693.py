def main(n):
    # Interpret n as both number of boys and number of girls: n -> (n, m) = (n, n)
    # Deterministic data generation
    m = n
    b = [i % 7 for i in range(1, n + 1)]
    g = [(i % 11) + 1 for i in range(1, m + 1)]

    if max(b) > min(g):
        # print(-1)
        pass
        return
    total = m * sum(b)
    b.sort()
    g.sort()
    while len(g) > 0:
        current = 0
        count = 1
        if len(b) > 0:
            current = b.pop()
        while len(g) > 0 and g[-1] > current and count < m:
            total += g[-1] - current
            g.pop()
            count += 1
        while len(g) > 0 and g[-1] == current:
            g.pop()
    # print(total)
    pass
if __name__ == "__main__":
    main(10)