import sys,math,itertools
from collections import Counter,deque,defaultdict
from bisect import bisect_left,bisect_right 
from heapq import heappop,heappush,heapify, nlargest
from copy import deepcopy
mod = 10**9+7
INF = float('inf')

def main(n):
    # 对于规模 n，构造：
    #   n: 第一行中的 n
    #   m: 第一行中的 m，设为 n
    #   c: 长度为 m 的 0..n-1 序列，循环取值
    m = n
    cnt = [0] * n
    c = [i % n for i in range(m)]
    for x in c:
        cnt[x] += 1
    print(min(cnt))

if __name__ == "__main__":
    main(10)