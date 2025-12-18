s1, s2 = input().split()
ans = 'z' * 21
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        ans = min(ans, s1[:i] + s2[:j])
print(ans)