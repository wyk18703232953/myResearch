def main(n):
    # Interpret n as the number of intervals; generate m and w deterministically
    # Ensure n >= 1 for meaningful behavior
    if n < 1:
        n = 1

    # Define m as a deterministic function of n
    m = 10 * n

    # Generate w as n increasing positions strictly between 0 and m
    # Example pattern: w[i] = floor((i+1)*m/(n+1))
    w = [(i + 1) * m // (n + 1) for i in range(n)]

    # Original algorithm begins here
    w = [0] + w + [m]
    c, d = [], []
    res = 0
    for j in range(n + 1):
        c.append(res)
        if j % 2 == 0:
            res += w[j + 1] - w[j]
    res = 0
    for j in range(n + 1, -1, -1):
        if j % 2 == 0 and j != n + 1:
            res += w[j + 1] - w[j]
        d.append(res)
    d = d[::-1]
    mx = d[0]
    for j in range(n + 1):
        mx = max(c[j] + (w[j + 1] - w[j] - 1) + (m - w[j + 1] - d[j + 1]), mx)
    # print(mx)
    pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10)