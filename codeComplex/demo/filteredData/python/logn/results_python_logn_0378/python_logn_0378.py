from math import gcd

MOD = 1000000007


def main(n: int):
    """
    n 为规模参数，这里用来生成测试数据 (x, k)：
    示例：x = n, k = n // 2
    可根据需要修改生成逻辑。
    """
    x = n
    k = n // 2

    if x == 0:
        # print(0)
        pass
        return

    x *= 2
    pow2k = pow(2, k, MOD)
    x = pow2k * x % MOD - (pow2k - 1)
    # print(x % MOD)
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(10)