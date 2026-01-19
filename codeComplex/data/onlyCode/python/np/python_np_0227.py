from itertools import combinations

n, l, r, x = map(int, input().split())
a = list(map(int, input().split()))

arr = []

for i in range(2, n+1):
    ar = combinations(a, i)
    for j in ar:
        arr += [(list(j))]

count = 0
for i in arr:
    dif = max(i) - min(i)
    total = sum(i)
    if dif >= x and (total >= l and total <= r):
        count +=1

print(count)
