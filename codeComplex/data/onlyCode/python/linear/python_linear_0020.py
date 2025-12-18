n = int(input())
arr = list(map(int, input().split()))
codd = 0
ceven = 0
ptodd = -1
pteven = -1
for i in range(n):
    if arr[i]%2 == 0:
        ceven += 1
        pteven = i
    else:
        codd += 1
        ptodd = i

if ceven == 1:
    print(pteven+1)
else:
    print(ptodd+1)