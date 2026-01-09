def main(n):
    # Interpret n as number of nodes
    m = n * 2  # deterministic choice of number of edges based on n

    # Deterministically generate m edges on n nodes (1-based to 1-based, then ignored)
    edges = []
    for i in range(m):
        a = (i % n) + 1
        b = ((i * 2) % n) + 1
        edges.append((a, b))

    ans = [0] * n
    for i in range(1, n, 2):
        ans[i] = 1
    # print(''.join(map(str, ans)))
    pass
if __name__ == "__main__":
    main(10)