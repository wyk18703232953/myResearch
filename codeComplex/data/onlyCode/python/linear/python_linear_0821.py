from collections import Counter

n, k = map(int, input().split())

for p in range(n+1):
    if p*(p+1)//2 - (n-p) == k:
        print(n-p)
        break
