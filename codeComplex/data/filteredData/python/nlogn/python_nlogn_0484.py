def main(n):
    # Interpret n as the number of elements in array a
    # Deterministic data generation: people and a
    people = n // 2 + 1  # deterministic function of n
    a = [(i % (n // 3 + 1)) + 1 for i in range(n)]

    a.sort()
    d = {}
    tmp = []
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    d1 = {}
    for i in d:
        if d[i] in d1:
            d1[d[i]] += 1
        else:
            d1[d[i]] = 1
        tmp.append(d[i])
    tmp.sort()
    ans = 0
    for i in range(1, 10001):
        x = people
        try:
            x -= d1[i]
        except KeyError:
            pass
        for j in d1:
            if j > i:
                x -= (j // i) * d1[j]
        if x <= 0:
            ans = max(ans, i)
    print(ans)
    return ans

if __name__ == "__main__":
    main(1000)