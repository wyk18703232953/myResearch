import sys

n, q = list(map(int,sys.stdin.readline().strip().split()))
a = list(map(int,sys.stdin.readline().strip().split()))
m = [0] * q

M = max(a)
i = 0
x = a[0]
L = []
L1 = []
L2 = []
while x != M:
    L1.append(x)
    L2.append(a[i+1])
    i = i + 1
    if x < a[i]:
        L.append(x)
        x = a[i]
    else:
        L.append(a[i])

b = a[i+1:] + L

for j in range (0, q):
    m = int(sys.stdin.readline().strip())
    if m <= i:
        print(str(L1[m-1]) + " " + str(L2[m-1]))
    else:
        print(str(x) + " " + str(b[(m - i - 1) % (n-1)]))
