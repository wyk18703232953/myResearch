from math import sqrt
n, k = map(int, input().split())
print(int(n - 0.5 * (sqrt(8 * (k + n) + 9) - 3)))
