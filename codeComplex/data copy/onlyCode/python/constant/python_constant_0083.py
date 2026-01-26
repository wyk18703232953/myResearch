n=int(input())
if n==1 or n==2 :
    print(n)
elif n%2!=0 :
    m=n*(n-1)*(n-2)
    print(m)
elif n%3!=0 :
    m=n*(n-1)*(n-3)
    print(m)
else :
    m=(n-1)*(n-2)*(n-3)
    print(m)