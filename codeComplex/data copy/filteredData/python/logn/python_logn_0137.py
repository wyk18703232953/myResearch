import time
from decimal import Decimal

def computeSum(x, k):
    return Decimal(((Decimal(x) / Decimal(2)) * Decimal(k - x + 1 + k)) - (x - 1))

def minSplitters(n, k):
    if n == 1:
        return 0
    elif n <= k:
        return 1
    max_sum = computeSum(k, k)
    if n > max_sum:
        return -1

    else:
        low = 0
        high = k
        while low < high:
            mid = (low + high) // 2
            previousSum = computeSum(mid - 1, k)
            currentSum = computeSum(mid, k)
            if currentSum == n:
                return mid
            elif currentSum < n:
                low = mid + 1
            elif currentSum > n:
                if previousSum >= n:
                    high = mid - 1

                else:
                    return mid
        return low

def main(n):
    # 将 n 作为规模参数：
    # 设 n 为原问题中的 n，k 由 n 确定性生成
    # 例如：k = n，用于可规模化实验
    k = n
    result = minSplitters(n, k)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)