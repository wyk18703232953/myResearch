def main(n):
    # Interpret n as number of nodes; ensure n >= 2 for edges
    if n < 2:
        n = 2

    # Deterministically set s based on n
    s = n

    # Initialize adjacency list
    v = [[] for _ in range(n + 1)]

    # Deterministically generate a tree:
    # Connect node i to node i//2 for i from 2 to n (a rooted tree)
    for i in range(2, n + 1):
        a = i
        b = i // 2
        v[a].append(b)
        v[b].append(a)

    # Count leaves
    ans = 0
    for i in range(1, n + 1):
        if len(v[i]) == 1:
            ans += 1

    # To mirror original behavior, use float division
    if ans == 0:
        result = 0.0

    else:
        result = 2 * s / ans

    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)