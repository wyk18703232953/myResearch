def result(a, b):
    if a == 0 or b == 0:
        return 0
    if a > b:
        return a // b + result(a % b, b)
    else:
        return b // a + result(b % a, a)


def main(n):
    """
    n 为规模参数，用来生成测试数据 (a, b)。
    这里简单地根据 n 构造一对正整数：
      a = n + 1
      b = 2 * n + 3
    如需不同的测试方式，可自行修改生成逻辑。
    """
    a = n + 1
    b = 2 * n + 3
    print(result(a, b))


if __name__ == "__main__":
    # 示例：用某个固定规模调用 main
    main(10)