def main(n: int):
    """
    n 用作生成测试数据的规模参数。
    这里示例地用 n 生成 x, k：
      x = n
      k = n 的二进制长度
    可按需要自行修改生成规则。
    """
    modulo = 10**9 + 7

    # 根据 n 生成测试数据（示例规则）
    x = n
    k = max(0, n.bit_length())  # 确保 k 为非负整数

    if x == 0:
        result = 0

    else:
        x %= modulo
        result = pow(2, k, modulo) * (2 * x - 1) + 1
        result %= modulo

    # print(result)
    pass
if __name__ == "__main__":
    # 可以在这里指定 n 进行简单测试
    main(10)