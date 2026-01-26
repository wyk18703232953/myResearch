from collections import defaultdict
from itertools import accumulate
import sys
input = sys.stdin.readline
'''
for CASES in range(int(input())):
n, m = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))
S = input().strip()
sys.stdout.write(" ".join(map(str,ANS))+"\n")
'''
inf = 100000000000000000  # 1e17
mod = 998244353

n, m ,k= map(int, input().split())
M=[]
S=[]
F=[]
for i in range(n):
    M.append(input().strip())
for i in range(m):
    tmp1, tmp2 = input().split()
    S.append(tmp1)
    F.append(int(tmp2)-1)


TRAN_dict=defaultdict(int)
TRAN_dict['_']=0
for i in range(97,97+26):
    TRAN_dict[chr(i)]=i-96;


def cal(X):
    base=1
    number=0
    for x in X:
        number=number*base+TRAN_dict[x]
        base*=27
    return number

STONE=defaultdict(int)
for i in range(n):
    STONE[cal(list(M[i]))]=i


def check(X,result):
    number=cal(X)
    if number in STONE.keys():
        result.append(STONE[number])

bian=[[] for i in range(n)]
du=[0]*n


for i in range(m):
    gain=[]
    for digit in range(1<<k):
        now=list(S[i])
        tmp=bin(digit)
        tmp=tmp[2:]
        tmp='0'*(k-len(tmp))+tmp
        for j in range(k):
            if tmp[j]=='1':
                now[j]='_'
        check(now,gain)
    if F[i] not in gain:
        print("NO")
        sys.exit(0)
    for x in gain:
        if x!=F[i]:
            bian[F[i]].append(x)
            du[x]+=1

from collections import deque
QUE=deque()
for i in range(n):
    if du[i]==0:
        QUE.append(i)
TOP_SORT=[]
while QUE:
    now=QUE.pop()
    TOP_SORT.append(now)
    for to in bian[now]:
        du[to]-=1
        if du[to]==0:
            QUE.append(to)
if len(TOP_SORT)==n:
    print("YES")
    print(*[i+1 for i in TOP_SORT])
else:
    print("NO")
