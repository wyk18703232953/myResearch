def main(n):
    # Generate deterministic input data based on n
    # Here, l and r are integer lists of length n
    # Example pattern: l[i] = i % 3, r[i] = (n - 1 - i) % 3
    l = [i % 3 for i in range(n)]
    r = [(n - 1 - i) % 3 for i in range(n)]

    a = [[l[i] + r[i], i] for i in range(n)]
    a.sort()
    candies = [0 for _ in range(n)]

    if n == 0:
        # print("YES")
        pass
        # print()
        pass
        return

    if a[0][0] != 0:
        # print("NO")
        pass
        return

    else:
        candies[a[0][1]] = n - a[0][0]

    for i in range(1, n):
        if a[i][0] != a[i - 1][0] and a[i][0] != i:
            # print("NO")
            pass
            return
        candies[a[i][1]] = n - a[i][0]

    for i in range(n):
        l1 = 0
        r1 = 0
        for j in range(i):
            if candies[j] > candies[i]:
                l1 += 1
        for j in range(i + 1, n):
            if candies[j] > candies[i]:
                r1 += 1
        if l1 != l[i] or r1 != r[i]:
            # print("NO")
            pass
            return

    # print("YES")
    pass
    # print(*candies)
    pass
if __name__ == "__main__":
    # Example deterministic call for experimental use
    main(10)