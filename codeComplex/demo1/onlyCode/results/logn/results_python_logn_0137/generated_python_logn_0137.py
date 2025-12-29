import time
from decimal import Decimal
import random

def main(n):
    # 生成测试数据：从 1 到 n 中随机选择 n 和 k（保证 k >= 1）
    # 原代码是读入 n, k；这里我们假设规模参数 n 作为 n 的上界，
    # 随机生成一个合法的 (n_val, k_val) 用于测试。
    if n < 2:
        n_val = 1
        k_val = 1
    else:
        n_val = random.randint(1, n)
        k_val = random.randint(1, n)

    computeSum = lambda x: Decimal(((Decimal(x) / Decimal(2)) *
                                   Decimal(k_val - x + 1 + k_val)) - (x - 1))

    def minSplitters():
        if n_val == 1:
            return 0
        elif n_val <= k_val:
            return 1

        max_sum = computeSum(k_val)
        if n_val > max_sum:
            return -1
        else:
            low = 0
            high = k_val
            while low < high:
                mid = (low + high) // 2
                previousSum = computeSum(mid - 1)
                currentSum = computeSum(mid)
                if currentSum == n_val:
                    return mid
                elif currentSum < n_val:
                    low = mid + 1
                else:
                    if previousSum >= n_val:
                        high = mid - 1
                    else:
                        return mid
            return low

    # 返回 (测试用的 n, k, 以及计算结果)，也可以只返回结果
    return n_val, k_val, minSplitters()

if __name__ == "__main__":
    # 示例：规模 100
    print(main(100))