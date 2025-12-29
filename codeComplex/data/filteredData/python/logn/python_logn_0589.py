import math
from collections import OrderedDict
import random

def main(n):
    # 生成测试数据：从 0 到 n 中随机选取 k
    k = random.randint(0, n)

    # 原逻辑：给定 n, k，找到满足条件的 i 并输出 n-i
    for i in range(1, n + 1):
        if (i * (i + 1)) // 2 - n + i == k:
            print(n - i)
            break

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)