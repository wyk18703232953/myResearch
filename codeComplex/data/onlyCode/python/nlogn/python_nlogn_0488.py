n, m = map(int, input().split())
a = list(map(int, input().split()))
dict = {i:0 for i in set(a)}
for i in range(m):
    dict[a[i]] += 1
k = 1
while sum(dict[i]//k for i in dict) >= n:
    k += 1
print(k - 1)
