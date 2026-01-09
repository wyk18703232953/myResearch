def main(n):
    # Interpret n as the length of array a
    # Deterministic construction:
    # - let c be a fixed color, e.g., 1
    # - array a cycles through values 1..K where K is bounded, e.g., 10
    c = 1
    K = 10
    a = [(i % K) + 1 for i in range(n)]

    # Core logic from original program
    f = [0] * 500001
    l = [[0] for _ in range(500001)]
    m = 0

    for i in range(n):
        val = a[i]
        if val < 500001:
            l[val].append(f[val] - m)
            if val == c:
                m += 1
            f[val] += 1
            l[val].append(f[val] - m)

    ma = 0
    for arr in l:
        mi = 0
        for v in arr:
            if v < mi:
                mi = v
            if ma < v - mi:
                ma = v - mi

    # print(m + ma)
    pass
if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(100000)