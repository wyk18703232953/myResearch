from math import ceil

n, k = map(int, input().split())

print(ceil((8 * n) / k) + ceil((5 * n) / k) + ceil((2 * n) / k))
