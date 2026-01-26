n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
while len(a) > 0:
    k = a.pop(0)
    a = [i for i in a if i % k != 0]
    ans += 1

print(ans)
