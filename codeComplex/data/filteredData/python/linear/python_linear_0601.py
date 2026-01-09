def main(n: int):
    # 生成规模为 n 的测试数据
    # 原程序中 n 来自 input()，这里直接使用传入的 n

    if n <= 10:
        for i in range(n):
            # print(0, i)
            pass
        return

    # n > 10 的情况
    # print(0, 0)
    pass
    for i in range(4, n + 1, 3):
        k = (i // 3) * 2
        # print(k, 0)
        pass
        # print(k - 1, 1)
        pass
        # print(k - 2, 2)
        pass

    k = ((n + 1) // 3) * 2
    if n % 3 == 0:
        # print(k - 1, 1)
        pass
        # print(k - 2, 2)
        pass
    elif n % 3 == 2:
        # print(k - 2, 2)
        pass


# 示例：调用 main 生成测试
if __name__ == "__main__":
    # 自行修改 n 测试规模
    test_n = 15
    main(test_n)