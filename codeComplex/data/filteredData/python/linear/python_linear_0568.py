def main(n):
    # Deterministically generate p as a parent array for a rooted tree:
    # For i >= 2, set parent p[i] = i // 2 (forms a binary-heap-like tree)
    if n <= 0:
        return
    p = [0, 0] + [i // 2 for i in range(2, n + 1)]
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
    # Example call for time-complexity experiments
    main(10)