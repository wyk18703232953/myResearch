a=''.join(reversed(sorted(input())))
b=int(input())
r=''
while len(a)>0:
    for i in range(len(a)):
        n=r+a[i]+''.join(sorted(a[:i]+a[i+1:]))
        if int(n)<=b:
            r+=a[i]
            a=a[:i]+a[i+1:]
            break
print(r)