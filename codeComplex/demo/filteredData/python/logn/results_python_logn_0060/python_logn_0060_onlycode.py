l, r = map(int, input().split())

ans = 0
for i in range(63, -1, -1):
    if r & (1 << i) > 0 and l & (1 << i) == 0:
        ans = (1 << (i + 1)) - 1
        break
print(ans)
