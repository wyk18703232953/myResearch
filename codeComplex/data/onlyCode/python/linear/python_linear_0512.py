n = int(raw_input())
a = list(raw_input())
b = list(raw_input())

ans = 0

for i in range(n - 1):
    if a[i] == b[i]:
        continue
    if a[i + 1] == b[i + 1]:
        continue

    if a[i] == b[i + 1] and a[i + 1] == b[i]:
        a[i], a[i + 1] = a[i + 1], a[i]
        ans += 1


for i in range(n):
    ans += a[i] != b[i]

print(ans)
