n, k = [int(e) for e in input().split()]
a = sorted([int(e) for e in input().split()])
s = set()
for i in range(n):
    if a[i] % k != 0:
        s.add(a[i])
    elif a[i] / k not in s:
        s.add(a[i])
print(len(s))