import sys
input = sys.stdin.readline

n, a, b = [int(i) for i in input().split()]
h = sorted([int(i) for i in input().split()])
Vasya = h[:b]
Petya = h[b:]
print(Petya[0] - Vasya[-1])
