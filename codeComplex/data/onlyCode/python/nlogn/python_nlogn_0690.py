from sys import exit
N, M = map(int, input().split())
B = list(map(int, input().split()))
G = list(map(int, input().split()))
B.sort()
mB = B[-1]
m2B = B[-2]
mG = min(G)
if mB > mG:
    print(-1)
    exit()
if mB == mG:
    print(sum(B)*M + sum(G) - mB * M)
    exit()
print(sum(B)*M + sum(G) - mB * M + mB - m2B)