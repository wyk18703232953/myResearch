a = list(input())
b = int(input())
a.sort(reverse=True)
# print(a)
ans=''
while a:
    for i in range(len(a)):
        temp=''
        x=ans+a[i]+temp.join(sorted(a[:i]+a[i+1:]))
        if int(x)<=b:
            ans+=a[i]
            a=a[:i]+a[i+1:]
            break
print(int(ans))