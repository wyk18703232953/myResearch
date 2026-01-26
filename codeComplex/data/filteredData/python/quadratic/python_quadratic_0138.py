import sys,math,itertools
from collections import Counter,deque,defaultdict
from bisect import bisect_left,bisect_right 
from heapq import heappop,heappush,heapify, nlargest
from copy import deepcopy
mod = 10**9+7
INF = float('inf')

def generate_grids(n):
    grids = []
    for k in range(4):
        tmp = []
        for i in range(n):
            row_chars = []
            for j in range(n):
                val = (i + j + k) % 2
                row_chars.append(str(val))
            tmp.append("".join(row_chars))
        grids.append(tmp)
    return grids

def core_logic(s, n):
    res = INF
    for pt in itertools.combinations(range(4), 2):
        cnt = 0
        for k in range(4):
            f = 1 if k in pt else 0
            for i in range(n):
                for j in range(n):
                    if (i + j + f) % 2 != int(s[k][i][j]):
                        cnt += 1
        res = min(res, cnt)
    return res

def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    s = generate_grids(n)
    res = core_logic(s, n)
    # print(res)
    pass
if __name__ == "__main__":
    main(5)