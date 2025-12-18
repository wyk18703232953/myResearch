n = int(input())
lst = list(map(int,input().split()))
lst.sort()
lst.reverse()
m = 0
for i in range(n):
  if sum(lst[:i]) > sum(lst[i:]):
    break
  else:
    m+=1
print(m)