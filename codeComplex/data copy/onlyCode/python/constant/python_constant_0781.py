t=int(input())
k=set()
for i in range(1,10**5):
  k.add(4*i*i)
  k.add(2*i*i)
for _ in range(t):
  n=int(input())
  if n in k:
    print('YES')
  else:
    print('NO')