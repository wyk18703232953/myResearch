import random

def main(n: int):
    """
    n 为规模参数，用于生成测试数据：
    - x 在 [0, 10^n] 范围内随机生成
    - k 在 [0, n] 范围内随机生成
    """
    # 生成测试数据
    upper_x = 10 ** n
    x = random.randint(0, upper_x)
    k = random.randint(0, n)

    # 原始逻辑
    if x == 0:
        print(0)
        return

    mod = 10 ** 9 + 7
    a = ((x % mod) * pow(2, k + 1, mod)) % mod
    result = (a - (pow(2, k, mod) - 1)) % mod

    print(result)


if __name__ == "__main__":
    # 示例：使用 n=5 运行
    main(5)