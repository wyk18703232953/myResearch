a,b = list(input()),int(input())
ans = ""
a.sort(reverse=True)
while len(a)>0:
    for i in range(len(a)):
        num = ans+a[i]+"".join(sorted(a[:i]+a[i+1:]))
        if int(num)<=b:
            ans += a[i]
            a = a[:i]+a[i+1:]
            break
print(ans)