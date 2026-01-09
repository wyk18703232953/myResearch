def main(n):
    if n < 6:
        # print(-1)
        pass

    else:
        l = []
        o = []
        x = (3 + n) // 2
        for i in range(3, x + 1):
            l.append((1, i))
        for i in range(x + 1, n + 1):
            o.append((2, i))

        # print("1 2")
        pass
        for x_pair in l:
            # print(f"{x_pair[0]} {x_pair[1]}")
            pass
        for x_pair in o:
            # print(f"{x_pair[0]} {x_pair[1]}")
            pass

    # print("1 2")
    pass
    p = 2
    for i in range(3, n + 1):
        # print(f"{p} {i}")
        pass
        p = i


if __name__ == "__main__":
    # 示例：使用一个固定的 n 进行可重复实验
    main(10)