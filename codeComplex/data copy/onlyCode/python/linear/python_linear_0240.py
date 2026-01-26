from collections import Counter

def f(x):
    return max(list(Counter(x).values()))

n=int(input())
z=input()
l=len(z)
a=f(z)
b=f(input())
c=f(input())

def v(x):
    if x==l:
        return x-1
    else:
        return x+1

if n==1:
    a, b, c=v(a), v(b), v(c)
    if a>b and a>c:
        print("Kuro")
    elif b>a and b>c:
        print("Shiro")
    elif c>a and c>b:
        print("Katie")
    else:
        print("Draw")
elif (l-a<=n)+(l-b<=n)+(l-c<=n)>=2:
    print("Draw")
elif a>b and a>c:
    print("Kuro")
elif b>a and b>c:
    print("Shiro")
elif c>a and c>b:
    print("Katie")
else:
    print("Draw")
#print((l-a<=n)+(l-b<=n)+(l-c<=n))
#print(a, b, c)