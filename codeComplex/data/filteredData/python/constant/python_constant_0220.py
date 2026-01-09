def main(n):
    # 依据 n 确定性生成输入规模
    a = 2 * n + 1
    b = 3 * n + 2
    x = n
    y = n // 2
    z = n // 3

    if a < x * 2 + y:
        ry = x * 2 + y - a

    else:
        ry = 0

    if b < y + z * 3:
        rb = y + z * 3 - b

    else:
        rb = 0

    result = ry + rb
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)