from itertools import accumulate
n,m,k = map(int,input().split())
a = list(map(int,input().split()))
als = []
for i in range(m):
  ls = a[:]
  for j in range(n):
    if j%m == i:
      ls[j] -= k
  als.append(list(accumulate(ls)))
ans = 0
for i in range(m):
  ls = als[i]
  mn = 0
  anstmp = 0
  for j in range(n):
    if mn > ls[j]:
      mn = ls[j]
    if j%m == i:
      anstmp = max(anstmp,ls[j]-mn)
  ans = max(ans,anstmp)
print(ans)