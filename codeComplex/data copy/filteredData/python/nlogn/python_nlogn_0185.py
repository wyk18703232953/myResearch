def main(n):
    # n: length of the input array
    # Deterministic data generation: a[i] = (i % 5) - 2, for i in 1..n
    a = [(i % 5) - 2 for i in range(1, n + 1)]

    mp = {}
    s = 0
    ans = 0
    i = 0
    for x in a:
        i += 1
        s += x

        if x not in mp:
            mp[x] = 0
        if x + 1 not in mp:
            mp[x + 1] = 0
        if x - 1 not in mp:
            mp[x - 1] = 0

        mp[x] += 1

        adj = mp[x] + mp[x + 1] + mp[x - 1]
        c = s
        c -= mp[x] * x
        c -= mp[x + 1] * (x + 1)
        c -= mp[x - 1] * (x - 1)

        valid = i - adj
        ans += (valid * x) - c

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)