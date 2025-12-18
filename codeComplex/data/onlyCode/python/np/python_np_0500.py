import sys
I=sys.stdin.readlines()
N,M,K=map(int,I[0].split())
S=[I[i+1][:-1] for i in range(N)]
D=dict()
for i in range(N):
  D[S[i]]=i
T=[I[i+N+1].split() for i in range(M)]
for i in range(M):
  T[i][1]=int(T[i][1])-1
G=[[] for i in range(N)]
C=[0]*N
for i in range(M):
  for j in range(K):
    if S[T[i][1]][j]!='_' and S[T[i][1]][j]!=T[i][0][j]:
      print('NO')
      exit()
  for j in range(1<<K):
    t=''.join(['_' if j&(1<<k) else T[i][0][k] for k in range(K)])
    x=D.get(t,-1)
    if x!=-1 and x!=T[i][1]:
      G[T[i][1]].append(x)
      C[x]+=1
P=[]
Q=[]
F=[1]*N
for i in range(N):
  if C[i]==0 and F[i]:
    Q.append(i)
  while len(Q):
    v=Q.pop()
    F[v]=0
    P.append(v+1)
    for i in range(len(G[v])):
      C[G[v][i]]-=1
      if C[G[v][i]]==0:
        Q.append(G[v][i])
if len(P)==N:
  print('YES')
  print(*P)
else:
  print('NO')
