s=int(input())
t=len(str(s))
L=['4','7']
import copy
for i in range(t):
    L1=copy.deepcopy(L)
    for m in L:
        L1.append(m+'4')
        L1.append(m+'7')
    L=L1
L0=list(map(int,L))
sum=0
for i in range(len(L0)):
    if s%L0[i]==0:
        sum=sum+1
if sum>0:
    print('YES')
else:
    print('NO')