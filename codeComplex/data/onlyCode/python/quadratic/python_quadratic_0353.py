n = int(input())
s = list(input())
t = list(input())

if sorted(t) == sorted(s):
    ans = []
    for i in range(n-1, -1, -1):
        if t[i] != s[i]:
            j = s.index(t[i])
            for k in range(j, i):
                s[k], s[k+1] = s[k+1], s[k]
                ans.append(str(k+1))
    print(len(ans))
    print(' '.join(ans))
else:
    print(-1)
