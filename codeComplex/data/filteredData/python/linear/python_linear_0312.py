def main(n):
    # Interpret n as both the array length and modulus
    if n <= 0:
        print(0)
        print()
        return

    m = n
    a = [i % (2 * m + 1) for i in range(n)]

    t = n // m
    remain = [[] for _ in range(m)]
    for i in range(n):
        x = a[i] % m
        remain[x].append(i)

    ans = 0
    f = []
    for i in range(2 * m):
        cur = i % m
        while len(remain[cur]) > t:
            elm = remain[cur].pop()
            f.append([elm, i])
        while len(remain[cur]) < t and len(f) != 0:
            elm, j = f.pop()
            remain[cur].append(elm)
            delta = abs(i - j)
            a[elm] += delta
            ans += delta

    print(ans)
    print(*a)


if __name__ == "__main__":
    main(10)