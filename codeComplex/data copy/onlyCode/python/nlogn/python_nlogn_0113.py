n = int(input())
A = [int(a) for a in input().split()]
B = A.copy()
B.sort()
c = 0
for i in range(n):
    a = A[i]
    b = B[i]
    if a == b:
        continue
    else:
        c += 1
if c == 0 or c == 2:
    print("YES")
else:
    print("NO")