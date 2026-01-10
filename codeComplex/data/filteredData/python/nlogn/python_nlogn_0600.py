def main(n):
    # Interpret n as the size of the array a, and set m = n deterministically
    m = n
    # Deterministically generate array a of length n
    # Example: a[i] = (i % 7) + 1 so values are small positive integers
    a = [(i % 7) + 1 for i in range(n)]

    c = sum(a)
    if n == 1:
        print(0)
        return

    a.sort()
    res = 0
    pocl = a[n - 1]
    f = False
    for i in range(n - 2, -1, -1):
        if pocl > 1:
            if a[i] >= pocl:
                res += 1
                pocl -= 1
                res += (a[i] - 1)
            else:
                f = True
                pocl = a[i]
                res += 1
                res += (a[i] - 1)
                pocl -= 1
        elif pocl == 1:
            if f:
                res += 1
            res += (a[i] - 1)
            pocl -= 1
        else:
            res += (a[i] - 1)
    print(res)


if __name__ == "__main__":
    main(10)