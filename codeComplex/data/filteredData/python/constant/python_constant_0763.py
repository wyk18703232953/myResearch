from math import sqrt
import random

def main(n):
    # 生成测试数据：n 保持为规模参数，k 按某种规则生成
    # 这里示例设定：1 <= k <= n^2
    k = random.randint(1, max(1, n * n))

    # 原始逻辑
    result = int(n - 0.5 * (sqrt(8 * (k + n) + 9) - 3))

    print(result)


if __name__ == "__main__":
    # 示例：调用 main，规模设为 10
    main(10)