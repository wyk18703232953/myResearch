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
    # 映射规则：
    # 给定规模 n（n >= 1），构造一组 (N, K)
    # N 表示初始 n，K 表示参数 k
    # 为了稳定可扩展，将 N 与 K 设计成简单的算术序列
    if n < 1:
        n = 1
    # 这里 N 随 n 线性增大，K 为 n 的一半向下取整
    N = n * 10
    K = n // 2
    out = sol.solve(N, K)
    print(str(out))


if __name__ == "__main__":
    # 示例：以 n = 10 作为规模调用
    main(10)