a=[i for i in input()]
b=int(input())
a.sort(reverse=True)
ans = ''
while len(a) > 0:
    for i in range(len(a)):
        tmp = ans + a[i] + ''.join(sorted(a[:i] + a[i + 1:]))
        if int(tmp) <= b:
            ans += a[i]
            a = a[:i] + a[i + 1:]
            break
print(ans)
