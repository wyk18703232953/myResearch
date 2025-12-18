n = int(input())
A = [int(a) for a in input().split()]
B = A.copy()
B.sort()
c = 0
for i in range(n):
    c = c + 1 if A[i] != B[i] else c
print("YES" if c <= 2 else "NO")