def main(n):
    from bisect import bisect_right

    if n <= 0:
        return 0

    # Deterministic generation of x, y based on n
    x = n // 2 + 1
    y = n % 7 + 1

    # Generate n intervals deterministically
    s = [0] * n
    e = [0] * n
    for i in range(n):
        s[i] = i * 2
        e[i] = s[i] + (i % 5) + 1

    v = [0] * n
    c = 0
    for i in range(n):
        c += x + (e[i] - s[i]) * y

    s.sort()
    e.sort()

    for i in range(n - 2, -1, -1):
        k = bisect_right(s, e[i])
        while k < n and v[k] == 1 and (s[k] - e[i]) * y < x:
            k += 1
        if k == n:
            continue
        if (s[k] - e[i]) * y < x:
            v[k] = 1
            c += (s[k] - e[i]) * y - x

    result = c % (10**9 + 7)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)