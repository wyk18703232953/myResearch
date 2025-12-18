n, k = map(int, input().split())
li = [int(num) for num in input().split(" ", n - 1)]
ans = []
for i in range(0, n):
    su = 0
    for j in range(i, n):
        su += li[j]
        if (j - i + 1 >= k):
            ans.append(su / (j - i + 1))
print(max(ans))