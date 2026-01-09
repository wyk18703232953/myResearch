def main(n):
    # Interpret n as the size parameter; construct a deterministic (n, m) and m queries
    # Example scaling:
    #   - number of nodes: N = n
    #   - number of operations: M = n
    N = n
    M = n

    # Reuse variable names from original code
    max_dist = (N - 1) * N // 2
    min_dist = max_dist
    curr_value = max_dist

    for i in range(N):
        curr_value = i * (i + 1) // 2 + (N - 1 - i) * (N - i) // 2
        if curr_value < min_dist:
            min_dist = curr_value

    answer = 0
    add_value = 0

    # Deterministically generate M pairs (x, d)
    # For example:
    #   x_i = i
    #   d_i = (-1)**i * (i % (N + 1))  (alternating sign, bounded by N)
    for i in range(M):
        x = i
        d = (i % (N + 1))
        if i % 2 == 1:
            d = -d

        answer += x
        if d >= 0:
            add_value += d * max_dist

        else:
            add_value += d * min_dist

    result = answer + (add_value / N)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)