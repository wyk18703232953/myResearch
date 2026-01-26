# A. Game Shopping

n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0
i = 0
for bill in a:
    try:
        i += next(ind for ind, el in enumerate(c[i:]) if el <= bill) + 1
        ans += 1
    except StopIteration:
        break

print(ans)
