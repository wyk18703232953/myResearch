n = int(input())
l = [input() for _ in range(n)]
l.sort(key=lambda x: len(x))

ok = True
for i in range(n-1):
  if l[i] not in l[i+1]:
    ok = False
    break

if ok:
  print("YES")
  print(*l, sep='\n')
else:
  print("NO")
