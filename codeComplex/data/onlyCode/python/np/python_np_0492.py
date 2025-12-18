import sys
input = sys.stdin.readline

n,m,k=map(int,input().split())
P=[input().strip() for i in range(n)]
S=[input().split() for i in range(m)]

for i in range(m):
    S[i][1]=int(S[i][1])-1

PDICT=dict()
for i in range(n):
    PDICT[P[i]]=i

E=[]

for i in range(m):
    x=S[i][0]
    LIST=[]

    for j in range(1<<k):
        t=""
        for l in range(k):
            if (1<<l) & j != 0:
                t+="_"
            else:
                t+=x[l]

        if t in PDICT:
            LIST.append(PDICT[t])

    if not (S[i][1] in LIST):
        print("NO")
        exit()

    else:
        s=S[i][1]
        for l in LIST:
            if l==s:
                continue
            else:
                E.append((s,l))

EDGEIN=[0]*n # その点に入るEDGEの個数
EDGEOUTLIST=[[] for i in range(n)] # EDGEの行き先
for x,y in E:
    EDGEIN[y]+=1
    EDGEOUTLIST[x].append(y)

from collections import deque
QUE = deque()

for i in range(n):
    if EDGEIN[i]==0:
        QUE.append(i) # 行き先のない点をQUEに入れる
        
TOP_SORT=[]
while QUE:
    x=QUE.pop()
    TOP_SORT.append(x) # 行き先がない点を答えに入れる
    for to in EDGEOUTLIST[x]:
        EDGEIN[to]-=1 # 行き先がない点を削除し,そこから一歩先の点のEDGEINを一つ減らす.
        if EDGEIN[to]==0:
            QUE.appendleft(to)

if len(TOP_SORT)==n:
    print("YES")
    print(*[i+1 for i in TOP_SORT])
else:
    print("NO")
        
