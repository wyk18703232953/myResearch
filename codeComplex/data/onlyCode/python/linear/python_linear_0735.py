from collections import defaultdict as dd, deque
import sys,atexit
from io import BytesIO
inp = BytesIO(sys.stdin.buffer.read())
input = lambda:inp.readline().decode('ascii')
buf = BytesIO()
sys.stdout.write = lambda s: buf.write(s.encode('ascii'))
atexit.register(lambda:sys.__stdout__.buffer.write(buf.getvalue()))

n,q = map(int,input().split())
S = [int(x) for x in input().split()]
Q = deque(S)

n = len(Q)
res = []
for i in range(n):
    a = Q.popleft()
    b = Q.popleft()
    Q.appendleft(max(a,b))
    Q.append(min(a,b))
    res.append((a,b))

A = list(Q)

def solve(t):
    if t < len(res):
        return res[t-1]
    t -= len(res) + 1
    t %= n-1
    return A[0],A[t+1]

for _ in range(q):
    t = int(input())
    print(*solve(t))
    
#def brute(t):
#    Q = deque(S)
#    for i in range(t):
#        a = Q.popleft()
#        b = Q.popleft()
#
#        Q.appendleft(max(a,b))
#        Q.append(min(a,b))
#    return a,b

#for i in range(1,1000):
#    assert brute(i) == solve(i)
