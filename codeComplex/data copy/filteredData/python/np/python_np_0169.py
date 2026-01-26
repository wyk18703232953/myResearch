def main(n):
    # Map n to problem parameters deterministically
    # Use n as number of elements
    if n <= 0:
        print(0)
        return

    # Deterministic construction of c, l, r, x based on n
    # c: strictly increasing sequence
    c = [i * 3 + 1 for i in range(n)]

    # Define l, r, x to scale with n and values in c
    total_sum = sum(c)
    min_sum = c[0] + c[1] if n >= 2 else c[0]
    max_sum = total_sum

    # Choose a window inside [min_sum, max_sum]
    l = min_sum + (total_sum - min_sum) // 4
    r = min_sum + (total_sum - min_sum) * 3 // 4

    # x is related to spread of values
    x = max(1, (c[-1] - c[0]) // 3)

    # Core algorithm (unchanged logic)
    c.sort()
    ans = 0
    for i in range(2 ** n):
        s = []
        for j in range(n):
            if i & (2 ** j):
                s.append(c[j])
        if s and sum(s) >= l and sum(s) <= r and max(s) - min(s) >= x:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main(10)