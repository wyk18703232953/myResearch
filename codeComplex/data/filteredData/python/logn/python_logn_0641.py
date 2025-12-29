import math
import random

def sportMafia(n, k):
    r = round(n + 1.5 - math.sqrt(2 * (n + k) + 2.75))
    return r

def main(n):
    # 根据规模 n 生成测试数据 (n_moves, k_candies)
    # 简单策略：n_moves = n，k 在 [0, n^2] 范围内随机
    n_moves = n
    # 确保 k 不为负且规模随 n 增长
    k_candies = random.randint(0, max(0, n_moves * n_moves))

    result = sportMafia(n_moves, k_candies)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main，规模可以在此修改或由外部调用 main(n)
    main(10)