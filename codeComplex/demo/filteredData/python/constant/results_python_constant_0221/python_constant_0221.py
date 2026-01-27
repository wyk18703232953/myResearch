def main(n):
    # 映射 n 为输入规模，这里用 n 生成 5 个确定性整数
    yellow = n
    blue = n + 1
    x = n + 2
    y = n // 2
    z = (n % 5) + 1

    ry = x * 2 + y
    rb = z * 3 + y
    r1, r2 = 0, 0
    if ry - yellow < 0:
        r1 = 0

    else:
        r1 = ry - yellow
    if rb - blue < 0:
        r2 = 0

    else:
        r2 = rb - blue
    # print(r1 + r2)
    pass
if __name__ == "__main__":
    main(10)