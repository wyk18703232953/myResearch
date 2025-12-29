import math
import random

def main(n: int) -> str:
    # 原逻辑：第 n 位数字（从 1 开始）在序列 "123456789101112..." 中的值
    k = 1
    while n > 9 * k * (10 ** (k - 1)):
        n -= 9 * k * (10 ** (k - 1))
        k += 1

    remainder = n % k
    if remainder == 0:
        remainder = k

    if k == 1:
        quoteint = math.ceil(n / k)
    else:
        adder = int("9" * (k - 1))
        quoteint = math.ceil(n / k) + adder

    return str(quoteint)[remainder - 1]


if __name__ == "__main__":
    # 根据规模 n 生成测试数据：
    # 这里假设 n 表示要测试的最大位置，生成若干随机位置进行测试。
    # 可根据需要调整测试策略。
    scale_n = 1000  # 规模，可按需修改
    test_positions = [1, 9, 10, 11, 190, 191, scale_n]  # 一些典型位置
    # 追加随机测试位置
    test_positions += [random.randint(1, scale_n) for _ in range(10)]

    for pos in test_positions:
        print(f"n = {pos}, digit = {main(pos)}")