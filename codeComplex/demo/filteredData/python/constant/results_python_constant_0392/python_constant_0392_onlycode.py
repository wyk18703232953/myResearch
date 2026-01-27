s = [list(input()), list(input())]
ans = 0
l = len(s[0])
i = 0
while i < l - 1:
    a = (s[0][i], s[0][i + 1], s[1][i], s[1][i + 1])
    if a.count("0") == 4:
        ans += 1
        s[0][i + 1] = "X"
        i+=1
    elif a.count("0") == 3:
        ans += 1
        i += 2
    else:
        i += 1
print(ans)
