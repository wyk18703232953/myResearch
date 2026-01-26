from math import gcd, ceil, sqrt
from itertools import combinations
from collections import Counter
from bisect import bisect_left, bisect_right

mod = 1000000007

def main(n):
    # n 表示数组长度
    if n <= 0:
        print(0)
        return

    arr = [i + 1 for i in range(n)]

    # 将 l, r, x 设计成随 n 确定变化的参数
    total_sum = n * (n + 1) // 2
    l = total_sum // 4
    r = total_sum * 3 // 4
    x = max(1, n // 4)

    count = 0
    for size in range(2, n + 1):
        for comb in combinations(arr, size):
            s = sum(comb)
            if l <= s <= r and max(comb) - min(comb) >= x:
                count += 1
    print(count)

if __name__ == "__main__":
    main(10)