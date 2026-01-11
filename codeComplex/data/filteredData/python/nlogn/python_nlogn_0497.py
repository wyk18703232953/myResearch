def main(n):
    # n: number of items
    # Deterministically generate m, a, b
    # Let a[i] = i + 3, b[i] = i % 5, m proportional to sum(a)
    a = [i + 3 for i in range(n)]
    b = [i % 5 for i in range(n)]
    sum_a = sum(a)
    # Choose m so that behavior scales with n
    m = sum_a * 2 // 3

    diff = [a[i] - b[i] for i in range(n)]
    diff.sort(reverse=True)

    i = 0
    while sum_a > m and i < n:
        sum_a = sum_a - diff[i]
        i += 1

    if i >= n and sum_a > m:
        # print(-1)
        pass

    else:
        # print(i)
        pass
if __name__ == "__main__":
    # Example: run with a moderate n for timing experiments
    main(10_000)