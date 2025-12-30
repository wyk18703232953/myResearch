def main(n: int) -> int:
    """
    根据规模 n 生成测试数据并返回计算结果。
    这里将“根据 n 生成测试数据”简单理解为：
    使用传入的 n 作为测试数据本身，然后执行原有逻辑。
    """
    # 原逻辑：num = n + n // 2
    num = n + n // 2
    return num


if __name__ == '__main__':
    # 示例：使用 n = 10 作为测试规模/测试数据
    test_n = 10
    result = main(test_n)
    print(result)