n, m = map(int, input().split())
A = list(map(int, input().split()))
L = [0]*n
for i in range(m):
    L[A[i]-1] += 1
print(min(L))