modulo = 1000 ** 3 + 7


def mat_oz(x, k):
    if k == 0:
        return (2 * x) % modulo
    if x == 0:
        return 0
    b = (pow(2, k, modulo) * (2 * x - 1) + 1) % modulo
    return b


def main(n: int):
    """
    n 为规模参数，用于生成测试数据。
    这里简单将:
      y = n
      m = n 的平方
    可根据需要修改生成规则。
    """
    y = n
    m = n * n
    result = mat_oz(y, m)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例: 使用 n = 10 运行
    main(10)