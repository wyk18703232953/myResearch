n, k = map(int, input().split())
lst = []
for i in range(n):
    a, b = map(int, input().split())
    lst.append([-a, b])
lst.sort()
print(lst.count(lst[k-1]))