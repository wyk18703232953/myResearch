def max1(a,b):
    if a>=b:
        return a,b
    else:
        return  b,a
def minus(a,b):
    p=a//b
    cnt=p
    return b,(a-(b*cnt)),cnt
n=int(input())
for _ in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    cnt=0

    while a>0 and b>0:
        a,b=max1(a,b)
        a,b,p=minus(a,b)
        cnt+=p

    print(cnt)
