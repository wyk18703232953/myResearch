n,m = map(int, input().split())
a= input()
b = input()
if '*' in a:
    c = a.replace('*','')
    i = a.index('*')
    if c==b:
        print("YES")
    elif a[:i]==b[:i]:
        t = a[i+1:]
        #print(t)
        tt = b[m - n+1+i:]
        #print(tt)
        if t ==tt and n-1<=m:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
elif n>m:
    print("NO")
else:
    if a==b:
        print("YES")
    else:
        print("NO")
