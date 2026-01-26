s1, s2 = input().split()
ans = s1[0]
for i in range(1, len(s1)):
    if s1[i] < s2[0]:
        ans += s1[i]
        if i == len(s1) - 1:ans += s2[0]
    else:
        ans += s2[0]
        break
if len(s1) == 1:print(s1[0] + s2[0])
else:print(ans)