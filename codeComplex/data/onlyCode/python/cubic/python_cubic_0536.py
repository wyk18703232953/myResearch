from collections import defaultdict
from collections import Counter
from collections import deque
import heapq

inf = float('inf')
ninf = float('-inf')

M1 = 10**9 + 7
M2 = 998244353

def li():
    return list(map(int,input().split()))

def pre():
    "Start"

def solve():
    a = input()
    b = input()
    n = len(a)
    if(len(a)<len(b)):
        a = sorted(list(a),reverse = True)
        print("".join(a))
        return
    b = int(b)
    ans = 0
    cnt = [0]*10
    for i in range(n):
        cnt[ord(a[i])-ord('0')] += 1

    def getrem(k):
        cnt[k] -= 1
        ans = ""
        for i in range(10):
            for j in range(cnt[i]):
                ans += str(i)
        cnt[k] += 1
        return ans

    prev = ""
    for i in range(n):
        for j in range(9,-1,-1):
            if(cnt[j]>0):
                newval = prev + str(j)+ getrem(j)
                if(int(newval)<=b):
                    ans = max(ans,int(newval))
                    prev += str(j)
                    cnt[j] -= 1
                    break
    print(ans)


pre()

__ = 1
#__ = int(input())
for _ in range(__):
    solve()