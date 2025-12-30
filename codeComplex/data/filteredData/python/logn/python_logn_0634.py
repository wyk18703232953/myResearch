#!/usr/bin/env python
# coding: utf-8
import random

def main(n):
    # 生成测试数据：随机生成 1 <= k <= n*(n+1)//2
    k = random.randint(1, n * (n + 1) // 2)

    def split_k(x):
        t = x + 1
        addition = t * (t + 1) // 2
        return addition - (n - x - 1) - k, n - x - 1

    j = 0
    while split_k(j)[0] != 0 and j < n - 1:
        j += 1

    result = split_k(j)[1]
    print(result)
    return result

if __name__ == "__main__":
    # 示例：可修改 n 以测试不同规模
    main(10)