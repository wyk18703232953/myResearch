s1, s2 = input().split()
ans = s1[0]
for i in range(1, len(s1)):
    if s1[i] < s2[0]:ans += s1[i]
    else:break
print(ans + s2[0])