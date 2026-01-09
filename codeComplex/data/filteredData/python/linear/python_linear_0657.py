def main(n):
    # Interpret n as the number of nodes in a tree (n >= 2)
    if n < 2:
        n = 2

    # Deterministic s based on n
    s = n * (n + 1) // 2

    # Deterministically generate a tree with n nodes
    # Here we use a simple star-shaped tree: node 1 connected to all others
    d = [0] * (n + 1)
    cnt = 0
    for i in range(2, n + 1):
        a, b = 1, i
        d[a - 1] += 1
        d[b - 1] += 1

    for i in range(0, n):
        if d[i] == 1:
            cnt += 1

    if cnt == 0:
        result = 0.0

    else:
        result = 2.0 * s / cnt

    # print(result)
    pass
if __name__ == "__main__":
    main(10)