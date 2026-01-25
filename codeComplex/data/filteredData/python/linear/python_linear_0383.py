from math import gcd,sqrt,factorial,pi,inf
from collections import deque,defaultdict
from bisect import bisect,bisect_left
from time import time
from itertools import permutations as per
from heapq import heapify,heappush,heappop,heappushpop

N = 10**9 + 7
lcm = lambda x,y:(x*y)//gcd(x,y)
inv = lambda x:pow(x,N-2,N)
sm = lambda x:(x**2+x)//2

def main(n):
    # 将 n 视为原程序中的 n
    # 构造确定性的 k 和 (x,d) 序列，用于测试算法时间复杂度
    if n <= 0:
        return 0

    k = max(1, n // 2)

    x_vals = [i % 10 for i in range(k)]
    d_vals = [((i % 2) * 2 - 1) * (i % 5) for i in range(k)]

    s = 0
    for i in range(k):
        x = x_vals[i]
        d = d_vals[i]
        s += n * x
        if d < 0:
            s += sm(n // 2) * d + sm(n // 2 - (n + 1) % 2) * d
        else:
            s += sm(n - 1) * d
    return s / n

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值
    result = main(10)
    print(result)