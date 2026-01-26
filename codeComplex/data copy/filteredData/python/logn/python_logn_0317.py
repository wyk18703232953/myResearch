MOD = 1000000007

def main(n):
    """
    n 作为规模参数，用于生成测试数据 (x, k)。
    这里采用一种简单的可重复生成方式：
      x = n
      k = n * n
    如需其他生成方式，可自行修改。
    """
    x = n
    k = n * n

    if x == 0:
        # print(0)
        pass
        return

    b = pow(2, k, MOD)
    a = (2 * x - 1) % MOD
    # print((a * b + 1) % MOD)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)