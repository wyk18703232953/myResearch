# alpha = "abcdefghijklmnopqrstuvwxyz"
# prime = 998244353 
INF = 1000_000_000

# from heapq import heappush, heappop
# from collections import defaultdict
# from math import sqrt
from collections import deque      
    
t = 1#int(input())

for test in range(t):
    # n = int(input())
    n,q = map(int, input().split())
    arr = list(map(int, input().split()))
    maxval = max(arr)
    d = deque(arr)
    ans = {}
    count = 1
    # print("check",d[0], maxval)
    while d[0]!=maxval:
        a = d.popleft()
        b = d.popleft()
        ans[count] = (a,b)
        count+=1
        d.append(min(a,b))
        d.appendleft(max(a,b))
    n = n-1
    for i in range(q):
        m = int(input())
        if m in ans:
            print(ans[m][0],ans[m][1])
        else:
            m = m - count
            print(maxval, d[1+(m%n)])
