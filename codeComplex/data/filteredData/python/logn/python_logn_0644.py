import collections
import heapq
import bisect
import math
import time

class Solution2:

    def solve(self, s):
        pass
        

class Solution:

    def solve(self, n, k):
        grow = 1
        tot = 0
        while n != tot - k:
            tot += grow
            grow += 1
            n -= 1
        return tot - k


def main(n):
    sol = Solution()
    # 将 n 映射为 N 和 K 的规模
    # 例如：N = n，K = n // 2
    N = n
    K = n // 2
    out = sol.solve(N, K)
    # print(str(out))
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小进行实验
    main(10)