s = input()
ans = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        cur = s[i:j]
        if cur in s[:(j - 1)] or cur in s[(i + 1):]:
            ans = max(ans, j - i)
print(ans)
