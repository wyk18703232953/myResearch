from math import ceil
N = int(input())
S = (N * (N + 1)) / 2
F = int(ceil(N /2.0))
ans = int((S + F) / 2)
print(ans)