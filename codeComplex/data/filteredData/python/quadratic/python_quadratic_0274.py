def main(n):
    # n controls the size of the lists x and y
    # Generate deterministic data
    # x: [0, 1, 2, ..., n-1]
    # y: [n//2, n//2+1, ..., n//2 + n - 1]
    m = n
    x = [i for i in range(n)]
    y = [n // 2 + i for i in range(m)]

    xx = set(x)
    yy = set(y)
    common = xx.intersection(yy)
    for i in x:
        if i in common:
            # print(i, end=' ')
            pass
    if n > 0:
        # print()
        pass
if __name__ == "__main__":
    main(10)