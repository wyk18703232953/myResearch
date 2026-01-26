n, d = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
Ans = 2
for i in range(1, n):
    if lst[i] - lst[i - 1] > 2 * d:
        Ans += 2
    elif lst[i] - lst[i - 1] == 2 * d:
        Ans += 1
print(Ans)
