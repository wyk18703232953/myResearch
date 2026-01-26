import sys
readline = sys.stdin.readline

N = int(readline())
M = float(readline())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))
B = B[1:] + [B[0]]
C = []
for a, b in zip(A[::-1], B[::-1]):
    C.append(b)
    C.append(a)

if 1 in C:
    print(-1)
else:
    M0 = M
    for c in C:
        M += M/(c-1)
    
    print(M-M0)