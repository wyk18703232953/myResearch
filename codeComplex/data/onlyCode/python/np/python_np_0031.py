n = int(input())
a = list(map(int,input().split()))
mod = 10**9+7
b = [0 for i in range(1<<20)]
for i in range(n):
  b[a[i]] += 1
for i in range(20):
  for j in range(1<<20):
    if j&1<<i == 0:
      b[j] += b[j|1<<i]
ans = 0
for i in range(1<<20):
  cnt = str(bin(i)).count("1")
  if cnt%2 == 0:
    ans += pow(2,b[i],mod)-1
  else:
    ans -= pow(2,b[i],mod)-1
  ans %= mod
print(ans)