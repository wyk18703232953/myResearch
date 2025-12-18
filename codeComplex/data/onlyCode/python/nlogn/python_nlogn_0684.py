n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
s = sorted(list(map(int, input().split())))
if a[-1] > s[0]:
    print(-1)
else:
    if a[-1] == s[0]:
        print(sum(a[:-1])*m+sum(s))
    else:
        print(sum(a[:-2])*m+a[-2]*(m-1)+sum(s)+a[-1])
