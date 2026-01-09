def main(n):
    # Generate deterministic l and r for size n
    # Example pattern: l[i] = i % (n//2 + 1), r[i] = (n-1-i) % (n//2 + 1)
    if n <= 0:
        return

    base = n // 2 + 1
    l = [i % base for i in range(n)]
    r = [(n - 1 - i) % base for i in range(n)]

    cost = [(l[i] + r[i], i) for i in range(n)]
    cost.sort()

    CANDIES = [None] * n
    CANDIES[cost[0][1]] = n

    candy = n
    for i in range(1, n):
        if cost[i][0] == cost[i - 1][0]:
            CANDIES[cost[i][1]] = candy

        else:
            candy -= 1
            CANDIES[cost[i][1]] = candy

    check = 1
    for i in range(n):
        lc = 0
        rc = 0
        for j in range(i):
            if CANDIES[j] > CANDIES[i]:
                lc += 1
        for j in range(i + 1, n):
            if CANDIES[j] > CANDIES[i]:
                rc += 1

        if lc != l[i] or rc != r[i]:
            check = 0

    if check == 1:
        # print("YES")
        pass
        for c in CANDIES:
            # print(c, end=" ")
            pass
        # print()
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)