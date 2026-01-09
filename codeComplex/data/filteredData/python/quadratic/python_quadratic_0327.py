def main(n):
    # Deterministic generation of (n, d, k) based on n
    # Ensure valid ranges and some variation for experiments
    if n < 3:
        n_val = 3

    else:
        n_val = n

    # Choose k between 2 and 5 deterministically
    k = 2 + (n_val % 4)

    # Choose diameter d between 2 and min(n_val-1, 10) deterministically
    max_d = min(n_val - 1, 10)
    if max_d < 2:
        d = 2

    else:
        d = 2 + (n_val % (max_d - 1))

    # Now run the original core logic with generated n_val, d, k
    n, d, k = n_val, d, k

    if n < d + 1 or (d > 1 and k == 1):
        # print('NO')
        pass
        return

    edges = [(1, 2)]
    stack = []
    d2 = d / 2
    d21 = d2 + 1
    for node in range(2, d + 1):
        edges.append((node, node + 1))
        stack.append([node, d2 - abs(d21 - node), k - 2])
    next_i = d + 2
    while next_i <= n:
        if not stack:
            # print('NO')
            pass
            return

        node = stack[-1]
        i, remaining_depth, remaining_degree = node
        if remaining_depth == 0 or remaining_degree == 0:
            stack.pop()
            continue

        node[2] -= 1
        edges.append((i, next_i))
        stack.append([next_i, remaining_depth - 1, k - 1])
        next_i += 1

    # print('YES')
    pass
    # print('\n'.join('{} {}'.format(a, b) for a, b in edges))
    pass
if __name__ == "__main__":
    # Example scale parameter for experimentation
    main(10)