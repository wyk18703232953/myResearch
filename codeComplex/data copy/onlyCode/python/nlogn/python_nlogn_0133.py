n,m,k = [int(y) for y in input().split()]
a = [int(y) for y in input().split()]
a.sort(reverse=True)
no = 0
while k < m and no < n:
    k += a[no]-1
    no += 1
if k < m:
    print(-1)
else:
    print(no)