import math
import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 约束：保证 9 + 8*(n + k) >= 0
    # 随机生成一个较大的 k，使得表达式有意义
    # 这里令 k 在 [0, n^2] 范围内（可根据需要调整）
    k = random.randint(0, max(0, n * n))

    q = int(-3 + math.sqrt(9 + 8 * (n + k))) // 2
    r = n - q

    print(r)

# 示例：直接运行文件时的简单测试
if __name__ == "__main__":
    main(10)