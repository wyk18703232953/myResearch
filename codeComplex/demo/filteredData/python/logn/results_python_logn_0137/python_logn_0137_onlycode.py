import time
from decimal import Decimal
n,k = map(int,raw_input().split())

computeSum = lambda x: Decimal(((Decimal(x)/Decimal(2)) * Decimal(k-x+1 + k)) - (x-1))

def minSplitters():
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
            mid = (low+high)/2
            previousSum = computeSum(mid-1)
            currentSum = computeSum(mid)
            if currentSum == n:
                return mid
            elif currentSum < n:
                low = mid + 1
            elif currentSum > n:
                if previousSum >= n:
                    high = mid-1
                else:
                    return mid
        return low
print(minSplitters())