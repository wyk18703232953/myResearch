from sys import stdin,stdout
stdout.flush()
def qu(a,b):
    print("?",a,b)
    return int(input())
a=0
b=0
big=qu(a,b)
for i in range(29,-1,-1):
    x=2**i
    f=qu(a+x,b)
    l=qu(a,b+x)
    if l==f:
        if big==1:
            a+=x
        else:
            b+=x
        big=f
    elif f==-1:
        a+=x
        b+=x   
print("!",a,b)

