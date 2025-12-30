import time
from decimal import Decimal
import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 随机生成 k，保证 1 <= k <= 2n（只是一个合理范围，可根据需要调整）
    if n <= 0:
        raise ValueError("n must be positive")
    k = random.randint(1, max(1, 2 * n))

    computeSum = lambda x: Decimal(
        ((Decimal(x) / Decimal(2)) * Decimal(k - x + 1 + k)) - (x - 1)
    )

    def minSplitters(n, k):
        if n == 1:
            return 0
        elif n <= k:
            return 1
        max_sum = computeSum(k)
        if n > max_sum:
            return -1
        else:
            low = 0
            high = k
            while low < high:
                mid = (low + high) // 2
                previousSum = computeSum(mid - 1)
                currentSum = computeSum(mid)
                if currentSum == n:
                    return mid
                elif currentSum < n:
                    low = mid + 1
                else:  # currentSum > n
                    if previousSum >= n:
                        high = mid - 1
                    else:
                        return mid
            return low

    # 执行逻辑并输出结果
    result = minSplitters(n, k)
    print(result)
    return result

if __name__ == "__main__":
    # 示例：使用 n=10 运行
    main(10)