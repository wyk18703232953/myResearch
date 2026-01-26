n, s = map(int, input().rstrip().split())
if n <= s:
    print(0)
    exit()
for i in range(s, n + 2):
    l = 0
    for j in str(i):
        l += int(j)
    if i - l >= s:
        break
print(max(n - i + 1, 0))