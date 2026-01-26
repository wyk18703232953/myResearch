def main(n):
    # Interpret n as the number of elements
    if n <= 0:
        print(0)
        return

    # Deterministic generation of c, l, r, x based on n
    # c is a sorted list of n positive integers
    c = [(i * 2 + 3) for i in range(n)]
    c.sort()
    total_sum = sum(c)
    l = total_sum // 4
    r = (total_sum * 3) // 4
    x = max(1, n // 3)

    p = 1 << n
    cnt = 0
    for j in range(p):
        if j > 0 and j & (j - 1) != 0:
            list1 = []
            for k in range(n):
                if j & (1 << k):
                    list1.append(c[k])
            s = sum(list1)
            if l <= s <= r and list1[-1] - list1[0] >= x:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main(10)