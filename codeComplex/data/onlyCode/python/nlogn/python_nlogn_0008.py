n, t = map(int, input().split())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a-(b / 2), a+ (b / 2)))
 
arr.sort()
ans = 0
for i in range(1, n):
    if abs(arr[i][0] - arr[i - 1][1]) == t:
        ans += 1
    elif abs(arr[i][0] - arr[i - 1][1]) > t:
        ans += 2
print(ans + 2)