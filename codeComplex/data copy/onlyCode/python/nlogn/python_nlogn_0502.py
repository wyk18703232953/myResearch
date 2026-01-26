n, capacity = map(int,input().split())
a = [(0, 0)]*n

for i in range(n):
    x, y = map(int,input().split())
    a[i] = (x, y)

a.sort(key=lambda x: max(0, x[0] - x[1]))

current_sum = 0; i = n - 1; ans = 0
for x in a:
    current_sum += x[0] 

while i >= 0 and current_sum > capacity:
    ans += 1
    current_sum -= max(0, a[i][0] - a[i][1])
    i -= 1

if current_sum <= capacity:
    print(ans)
else:
    print(-1)