def main(n):
    # Ensure m >= 1
    if n <= 0:
        return
    # Define m as a function of n to control bucket size; here choose roughly sqrt(n)
    m = max(1, int(n**0.5))
    # Generate deterministic array a of length n
    # Pattern: a[i] = i % (2*m) to give varied residues
    a = [i % (2 * m) for i in range(n)]

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
    # print(ans)
    pass
    # print(*a)
    pass
if __name__ == "__main__":
    # Example call; adjust n to scale input size
    main(10)