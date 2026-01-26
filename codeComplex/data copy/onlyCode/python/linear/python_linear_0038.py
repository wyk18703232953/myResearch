n,k = map(int,input().split())
a = list(map(int,input().split()))

count = 0
b = {}
for i in range(n):
    if a[i] in b:
        b[a[i]] += 1
    else:
        b[a[i]] =1
    if b[a[i]] == 1:
        count += 1
    if count == k:
        break
#print("i=", i)
#print(b)


for j in range(n):
  if a[j] in b:
    b[a[j]] -= 1
#    print("j=", j)
#    print(b)
  if b[a[j]] == 0:
    break 
#  print("j=",j)
        
if count != k:
    print("-1 -1")
else:
  if n == 1:
    print(1,1)
  elif n == 2 and count == 2:
    print(1,2)
  else:
    print(j+1,i+1)  