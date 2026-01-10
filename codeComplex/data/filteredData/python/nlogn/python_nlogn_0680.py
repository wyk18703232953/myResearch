def main(n):
    # n controls both arrays' lengths and m
    if n < 2:
        n = 2
    m = n

    # deterministic generation of a and b
    a = [(i * 2 + 1) % (3 * n + 7) for i in range(n)]
    b = [(i * 3 + 2) % (4 * n + 11) for i in range(n)]

    a.sort()
    b.sort()
    a.reverse()
    b.reverse()
    if a[0] > b[-1]:
        print(-1)
    else:
        flag = True
        if b[-1] == a[0]:
            s = sum(b)
            flag = False
        else:
            s = sum(b) - b[-1] + a[0]
        if flag:
            s += (sum(a) - a[0]) * m + b[-1] - a[1]
        else:
            s += (sum(a) - a[0]) * m
        print(s)


if __name__ == "__main__":
    main(10)