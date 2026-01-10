def main(n):
    # Interpret n as the number of (a, b) pairs
    # Deterministically construct m and the pairs
    # Example scheme:
    #   m = n * (n // 2)
    #   a_i = i + 1
    #   b_i = (i // 2) + 1, but not exceeding a_i
    m = n * (n // 2)
    tup = []
    sm = 0
    for i in range(n):
        a = i + 1
        b = (i // 2) + 1
        if b > a:
            b = a
        sm += a
        diff = a - b
        tup.append([diff, a, b])

    tup.sort(reverse=True)
    ans = 0
    i = 0
    while sm > m and i < n:
        sm -= tup[i][1]
        sm += tup[i][2]
        i += 1
        ans += 1
    if sm <= m:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    main(10)