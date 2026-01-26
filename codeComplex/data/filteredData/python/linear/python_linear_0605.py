def main(n):
    # print('0 0')
    pass

    if n <= 1:
        return
    n -= 1
    k = n // 2
    p = n - k
    x = -k // 2
    while k > 0:
        if x != 0:
            # print(x, 0)
            pass
            k -= 1
        x += 1
    y = -p // 2
    while p > 0:
        if y != 0:
            # print(0, y)
            pass
            p -= 1
        y += 1

if __name__ == "__main__":
    main(10)