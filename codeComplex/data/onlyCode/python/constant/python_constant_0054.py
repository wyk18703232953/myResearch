def luckynumber(n):
    a=[]
    for i in range(4,n+1):
        r=i
        c=0
        while(r>0):
            x=r%10
            if x!=4 and x!=7:
                c=1
                break
            r=r//10
        if c==0:
            a.append(i)
    return a
n=int(input())
a=luckynumber(n)
for i in a:
    if n==i or n%i==0:
        print("YES")
        break
else:
    print("NO")

