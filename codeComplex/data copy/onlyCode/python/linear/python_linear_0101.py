s1, s2 = [str(j) for j in input().split()]
output = s1 + s2
for j in range(len(s1)):
    s = s1[:j + 1]
    for k in range(len(s2)):
        s += s2[k]
        if sorted([s, output])[0] == s:
            output = s
print(output)
