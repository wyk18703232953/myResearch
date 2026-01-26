import sys
input = lambda: sys.stdin.readline().rstrip()
#CF-E-00
#import numpy as np
#import heapq
#from collections import deque
#from collections import Counter as cnt
from collections import defaultdict as ddc
#from math import factorial as fct
#from math import gcd
#from bisect import bisect_left as bsl
#from bisect import bisect_right as bsr
#from itertools import accumulate as acc
#from itertools import combinations as cmb
#from itertools import permutations as pmt
#from itertools import product as prd
#from functools import reduce as red
#import sys
#sys.setrecursionlimit(10**9)  #再帰を多く使う(デフォルトは1000)
def main():
    n, m, k = map(int,input().split())  #k: length of following inputs

    def edges(s):
        Ans = set()
        for i in range(2**k):
            ans = ''
            for j in range(k):
                if i>>j&1:
                    ans = ''.join([ans, s[j]])
                else:
                    ans = ''.join([ans, '_'])
            Ans.add(ans)
        return Ans

    D = ddc(lambda : -1)
    for i in range(n):
        D[input()] = i

    flag = 1
    In, Out = [set() for _ in range(n)], [set() for _ in range(n)]
    for _ in range(m):
        S, t = input().split()
        t = int(t)

        for e in edges(S):
            if D[e]+1:
                Out[t-1].add(D[e])
                In[D[e]].add(t-1)
        if t-1 not in Out[t-1]:
            flag = 0
            break
        else:
            Out[t-1].remove(t-1)
            In[t-1].remove(t-1)

    from collections import deque
    def topological_sort(In, Out):
        """
        Kahn, breadth first search
        In: 入力してくる頂点集合
        Out: 出力先の頂点集合
        """
        dq = deque()
        L = []
        for i, I in enumerate(In):
            if not I:
                dq.append(i)
        while dq:
            v = dq.popleft()
            L.append(v)
            for w in Out[v]:
                In[w].remove(v)
                if not In[w]:
                    dq.append(w)
        if len(L) < len(In):  #これはおかしい
            return False
        return L

    T = topological_sort(In, Out)
    if flag == 0 or not T:
        print('NO')
    else:
        print('YES')
        print(*[t+1 for t in T], sep = ' ')
        
main()