def check_number(x: int) -> str:
    # 原 main() 逻辑：判断 x 是否满足条件
    n = x
    if n % 2 == 1:
        return "NO"
    n //= 2
    if n == int(n ** 0.5) ** 2:
        return "YES"
    if n % 2 == 1:
        return "NO"
    n //= 2
    if n == int(n ** 0.5) ** 2:
        return "YES"
    return "NO"


def main(n: int):
    """
    n 为规模参数，这里用作测试数据的数量。
    根据 n 生成测试数据，并依次调用原逻辑。
    """
    # 生成测试数据：例如用 1 到 n 的整数作为测试用例
    test_cases = list(range(1, n + 1))

    for x in test_cases:
        print(check_number(x))


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)