import math
import random

def main(n):
    # 根据规模 n 生成测试数据
    # 这里将 n 作为原程序中的 n，
    # 并生成合理范围内的 k, s, p
    k = random.randint(1, max(1, n))      # 1 <= k <= n
    s = random.randint(1, max(1, n))      # 1 <= s <= n
    p = random.randint(1, max(1, n))      # 1 <= p <= n

    # 原始逻辑
    c = (n // s) if n % s == 0 else (n // s) + 1
    result = (c * k) // p if (c * k) % p == 0 else ((c * k) // p) + 1

    print(result)

if __name__ == "__main__":
    # 示例：调用 main，n 可按需修改或在其他地方被调用
    main(10)