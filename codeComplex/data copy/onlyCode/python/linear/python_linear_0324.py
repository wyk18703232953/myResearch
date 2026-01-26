from collections import Counter

n = int(input())
a = Counter()
b = Counter()
for _ in range(n):    
    a[input().strip()] += 1
for _ in range(n):
    b[input().strip()] += 1
ans = 0
for key in b:
    ans += max(b[key] - a[key], 0)
# print(a)
# print(b)
print(ans)