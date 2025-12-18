import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
from collections import defaultdict as dft


n,m,k=map(int,input().split())
dct={}
global case
case=0
iput=[]
for i in range(n):
    word=input()
    dct[word]=i+1
    iput.append(word)
d=[[] for i in range(n+1)]
size=[0]*(n+1)
for _ in range(m):
    
    word,idx=input().split()
    idx=int(idx)
    temp=1
    w=iput[idx-1]
    
    for x in range(k):
        if w[x]!='_' and w[x]!=word[x]:
            temp=0
            print("NO")
            exit()
            break
    
    
    res=[]
    for i in range(1<<k):
        s="".join([word[x] if i & (1<<x) ==0 else '_' for x in range(k)])
        #print(s)
        
        if s in dct:
            j=dct[s]
            if j!=idx:
                d[idx].append(j)
                size[j]+=1




st=[nd  for nd in range(1,n+1) if size[nd]==0]

for i in st:
    #print(st)
    for j in d[i]:
        size[j]-=1
        if size[j]==0:
            st.append(j)


if len(st)==n:
    print("YES")
    print(*st)
else:
    print("NO")
    

