def req_num(a, b, x, y, z):
    req_a = (x * 2) + y
    req_b = (z * 3) + y
    if (req_a - a) <= 0:
        ans_a = 0

    else:
        ans_a = req_a - a
    if (req_b - b) <= 0:
        ans_b = 0

    else:
        ans_b = req_b - b
    return ans_a + ans_b


def main(n):
    if n <= 0:
        n = 1
    a = n
    b = 2 * n
    x = n + 1
    y = 2 * n + 1
    z = 3 * n + 1
    result = req_num(a, b, x, y, z)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)