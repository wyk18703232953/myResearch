def main(n):
    # Interpret n as array length; choose k deterministically as max(1, n//3)
    if n <= 0:
        print(0.0)
        return
    k = max(1, n // 3)
    if k > n:
        k = n

    # Deterministic array generation
    a = [(i * 7 + 3) % 100 - 50 for i in range(n)]

    r = 0.0
    s = [0]
    for x in a:
        s.append(s[-1] + x)
    for i in range(n - k + 1):
        upper = min(n + 1, i + 2 * k)
        for j in range(i + k, upper):
            r = max(r, (s[j] - s[i]) / (j - i))
    print(r)


if __name__ == "__main__":
    # example call; adjust n as needed for experiments
    main(10)