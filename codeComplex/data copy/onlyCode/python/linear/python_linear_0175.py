n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
t = list(map(int, input().split()))
x = 0
summ = 0
maxx = 0
for i in range(n):
  summ += a[i]*t[i]
for i in range(k):
  if not t[i]:
    x+=a[i]
maxx = max(maxx,x)
for i in range(n-k):
  x+=a[i+k]*(1-t[i+k])
  x-=a[i]*(1-t[i])
  if x>maxx:
    maxx=x
  #maxx = max(x, maxx)
print(summ+maxx)