def main(n):
    # Interpret n as:
    # number of boys = n
    # number of girls = n (scale them equally)
    # Deterministic data generation
    boys = [i + 1 for i in range(n)]          # [1, 2, ..., n]
    girls = [i + n for i in range(n)]         # [n, n+1, ..., 2n-1]
    m = len(girls)

    boys.sort(reverse=True)
    girls.sort(reverse=True)
    s = sum(boys)
    ma = max(boys)
    res = 0

    # First loop
    for i in range(0, m):
        if girls[i] < ma:
            print(-1)
            return
        res += s
        if girls[i] == ma:
            girls[i] = 0

    # Second loop
    j = 0
    usage = 0
    for i in range(0, m):
        if usage == m - 1:
            j += 1
        if j >= n:
            print(-1)
            return
        res += max(0, girls[i] - boys[j])
        usage += 1

    print(res)


if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling/time experiments
    main(10)