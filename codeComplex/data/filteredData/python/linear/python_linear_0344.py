def main(n):
    # Deterministically generate d and array a based on n
    d = n // 3 + 1
    a = [i * 2 for i in range(n)]
    if n == 0:
        # print(0)
        pass
        return
    if n == 1:
        # print(2)
        pass
        return

    pos = 2
    for i in range(n - 1):
        l = a[i] + d
        r = a[i + 1] - d
        if l == r:
            pos += 1
        elif l < r:
            pos += 2
    # print(pos)
    pass
if __name__ == "__main__":
    main(10)