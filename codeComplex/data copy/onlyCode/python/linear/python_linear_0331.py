n, M = map(int, input().split())
A = list(map(int, input().split()))
A = [0]+A+[M]
D = []
for i in range(n+1):
    D.append(A[i+1]-A[i])
#print(D)
E = []
O = []
for i, d in enumerate(D):
    if i%2 == 0:
        E.append(d)
        O.append(0)
    else:
        O.append(d)
        E.append(0)
from itertools import accumulate
CE = [0]+E
CE = list(accumulate(CE))
CO = [0]+O
CO = list(accumulate(CO))

#print(CE)
#print(CO)
ans = CE[-1]
for i in range(n+1):
    if D[i] == 1:
        continue
    temp = CE[i]+(D[i]-1)+CO[-1]-CO[i+1]
    #print(i, temp)
    ans = max(ans, temp)
print(ans)
