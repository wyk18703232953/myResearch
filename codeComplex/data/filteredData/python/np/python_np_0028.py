import math
import random

MOD = 10 ** 9 + 7

# 预先已知的结果表（下标从 0 开始）
RES = [0, 1, 0, 3, 0, 15, 0, 133, 0, 2025, 0, 37851, 0, 1030367, 0, 36362925, 0]


def solve_for_n(n: int) -> int:
    """
    对单个 n 计算结果：
    result = RES[n] * n! mod MOD
    若 n 超出 RES 范围或 RES[n] 未定义，则返回 0。
    """
    if n < 0 or n >= len(RES):
        return 0
    return RES[n] * math.factorial(n) % MOD


def generate_test_data(n: int):
    """
    根据规模 n 生成测试数据。
    这里定义为：生成 1 到 n（或到已知表最大下标）的所有查询。
    可根据需要修改为随机数据。
    """
    max_index = min(n, len(RES) - 1)
    return list(range(1, max_index + 1))


def main(n: int):
    """
    封装整体逻辑：
    1. 根据 n 生成测试数据（若 n <= 0，则使用 n 本身作为单次测试）。
    2. 对每个测试数据调用 solve_for_n。
    3. 打印结果（逐行打印）。
    """
    if n <= 0:
        print(solve_for_n(0))
        return

    test_cases = generate_test_data(n)
    for x in test_cases:
        print(solve_for_n(x))


if __name__ == "__main__":
    # 示例：可根据需要手动修改测试规模
    main(10)