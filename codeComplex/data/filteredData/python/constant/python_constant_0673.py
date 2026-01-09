def qu(a, b, hidden_a, hidden_b):
    # print("?", a, b)
    pass

    if a >= hidden_a and b >= hidden_b:
        return -1
    if hidden_a > hidden_b:
        return 1
    if hidden_a < hidden_b:
        return -1
    return 0


def main(n):
    # 映射 n 为隐藏数对 (hidden_a, hidden_b)，确保确定性且规模随 n 增长
    hidden_a = n
    hidden_b = 2 * n

    a = 0
    b = 0
    big = qu(a, b, hidden_a, hidden_b)
    for i in range(29, -1, -1):
        x = 2 ** i
        f = qu(a + x, b, hidden_a, hidden_b)
        l = qu(a, b + x, hidden_a, hidden_b)
        if l == f:
            if big == 1:
                a += x

            else:
                b += x
            big = f
        elif f == -1:
            a += x
            b += x
    # print("!", a, b)
    pass
if __name__ == "__main__":
    main(10)