from itertools import combinations_with_replacement
import sys
import math
import bisect
import random

# 原始代码中的工具函数仍然保留（虽然本题逻辑基本用不到）
def BinarySearch(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

def main(n):
    """
    n 作为规模参数，这里用来控制测试数据的大小范围。
    例如：
      x 在 [0, n]
      k 在 [0, n]
    """
    # 根据 n 生成测试数据 (x, k)
    # 为了可复现，可以设定随机种子，如有需要可修改
    random.seed(0)
    x = random.randint(0, max(0, n))  # 保证非负
    k = random.randint(0, max(0, n))

    # 原始逻辑
    if x == 0:
        print(0)
    else:
        mod = (10**9) + 7
        a = pow(2, k, mod)
        b = ((2 * x) % mod - 1) % mod
        ans = ((a * b) % mod + 1) % mod
        print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)