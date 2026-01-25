def main(n):
    # Interpret n as the number of nodes; generate m and queries deterministically
    if n <= 0:
        return
    m = n  # scale number of queries with n

    # Original logic starts here, replacing all input() with deterministic generation
    max_dist = (n - 1) * n // 2
    min_dist = max_dist
    curr_value = max_dist
    for i in range(n):
        curr_value = i * (i + 1) // 2 + (n - 1 - i) * (n - i) // 2
        min_dist = min(min_dist, curr_value)

    answer = 0
    add_value = 0

    for i in range(m):
        # Deterministic generation of (x, d) based on i and n
        x = (i + 1) * (n % 7 + 1)
        d = (i % 5) - 2  # cycles through -2, -1, 0, 1, 2

        answer += x
        if d >= 0:
            add_value += d * max_dist
        else:
            add_value += d * min_dist

    result = answer + (add_value / n)
    print(result)


if __name__ == "__main__":
    main(10)