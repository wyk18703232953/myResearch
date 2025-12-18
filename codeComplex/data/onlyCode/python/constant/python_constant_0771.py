from math import sqrt

n, k = map(int, input().split())

answer = int(-1.5 + sqrt(9/4 + 2*(n+k)))

print(n - answer)
