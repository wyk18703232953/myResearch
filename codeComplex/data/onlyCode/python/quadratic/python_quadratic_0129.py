a, b = map(int, input().split())
arr = list(map(int, input().split()))
mn = float("inf")
for i in range(1, a+1):
    mn = min(mn, arr.count(i))

print(mn)


