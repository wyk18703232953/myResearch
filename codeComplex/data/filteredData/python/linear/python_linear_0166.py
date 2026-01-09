def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def main(n):
    """
    n 为规模参数，由调用者传入。
    本函数不进行任何 input() 调用，只根据 n 进行运算并输出结果。
    这里不额外生成复杂测试数据，直接使用 n 作为原程序中的输入。
    """
    # 原逻辑：若 n < 6 输出 -1，否则输出若干边
    if n < 6:
        # print(-1)
        pass

    else:
        for i in range(2, n - 2 + 1):
            # print(1, i)
            pass
        # print(2, n - 1)
        pass
        # print(2, n)
        pass

    for i in range(1, n):
        # print(i, i + 1)
        pass
if __name__ == "__main__":
    # 示例：根据需要自行修改这里的 n，用于本地测试
    test_n = 10
    main(test_n)