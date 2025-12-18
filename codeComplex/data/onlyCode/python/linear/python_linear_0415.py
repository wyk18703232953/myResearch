n, k = map(int, input().split())
s = input()
a = [0] * 26
for i in s:
    a[ord(i) - ord('a')] = 1
ans = 0
i = 0
while i < 26:
    if a[i] > 0:
        ans += i + 1
        k -= 1
        i += 1
        if k == 0:
            print(ans)
            break
    i += 1
else:
    print(-1)