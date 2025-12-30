def main(n: int):
    # 使用 n 作为原来程序中的 i
    i = n
    v = 0
    g = 2
    s = 4
    while g <= i:
        while s <= i:
            v = v + int(s / g * 4)
            s = s + g
        g = g + 1
        s = g * 2
    print(str(v))


if __name__ == "__main__":
    # 示例：自动生成一个规模为 10 的测试
    main(10)