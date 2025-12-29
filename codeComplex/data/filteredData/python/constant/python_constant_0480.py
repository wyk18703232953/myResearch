import random

def main(n: int) -> int:
    # 根据规模 n 生成测试数据
    # 这里约定：n 为人数，k 为糖果数，k 与 n 同量级
    if n <= 0:
        raise ValueError("n must be positive")

    # 生成 k，范围设为 [1, 10 * n]
    k = random.randint(1, 10 * n)

    # 原逻辑：计算向上取整的平均值 (k + n - 1) // n
    return (k + n - 1) // n


if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    result = main(10)
    print(result)