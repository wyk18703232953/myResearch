import math
import random

def main(n):
    # 生成测试数据：
    # 原公式中 k 需满足判别式非负：
    # (2n+3)^2 - 4(n^2 + n - 2k) >= 0
    # 化简得到：k ≥ 2 - 0.5n - 0.25n^2
    k_min = math.ceil(2 - 0.5 * n - 0.25 * n * n)
    # 为了多样性，向上取若干范围
    k_max = k_min + max(10, n)  # 简单给个上界
    k = random.randint(k_min, k_max)

    a = (2 * n + 3 - math.sqrt((2 * n + 3) ** 2 - 4 * (n ** 2 + n - 2 * k))) // 2
    print(int(a))

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)