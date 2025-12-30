def main(n: int):
    # 生成测试数据 m，这里简单设置为与 n 相关的一个值
    # 原程序中 m 未参与逻辑，仅为占位
    m = n * 2

    a = []
    b = []

    # 为保持逻辑一致，使用局部变量 cur_n 代替原来的 n（避免修改入参）
    cur_n = n

    if cur_n <= 8:
        a = [4]
        b = [5]

    while cur_n > 8:
        a += [4, 5]
        b += [5, 4]
        cur_n -= 8

    print(*a + [5], sep="")
    print(*b + [5], sep="")


if __name__ == "__main__":
    # 示例：调用 main，n 可根据需求调整
    main(20)