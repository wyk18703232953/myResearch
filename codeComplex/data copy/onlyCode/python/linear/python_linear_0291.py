n = int(input())
a = list(map(int, input().strip().split()))

b = set(a)
res = len(b)
if 0 in b:
    res -= 1
print(res)
