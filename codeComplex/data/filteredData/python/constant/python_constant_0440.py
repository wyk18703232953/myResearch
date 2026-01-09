def main(n: int):
    # 根据规模 n 生成测试数据：此处直接使用参数 n 作为原程序中的 n
    a = []
    b = []
    check = True
    cur = n

    # 原逻辑：不停地从 n 中减去 5 和 4，直到 n < 0
    while cur >= 0:
        if check:
            a.append(5)
            cur -= 5
            b.append(4)
            check = False

        else:
            check = True
            a.append(4)
            cur -= 4
            b.append(5)

    a.append(5)
    b.append(5)

    # print(*a, sep="")
    pass
    # print(*b, sep="")
    pass
if __name__ == "__main__":
    # 示例：以 n = 20 作为测试规模
    main(20)