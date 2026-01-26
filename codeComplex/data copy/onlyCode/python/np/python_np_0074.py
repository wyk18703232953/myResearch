a = input()
b = input()
l = a.count("+")-a.count("-")
k = b.count("?")
if k==0:
    if (b.count("+")-b.count("-"))==l:
        print(1)
    else:
        print(0)
else:
    n=2**k
    r=k
    c=[]
    t=0
    while r>=0:
        c.append(r-t)
        t+=1
        r-=1
    import math
    d=[]
    for i in range(k+1):
        d.append((math.factorial(k))//(math.factorial(i)*math.factorial(k-i)))
    f = b.count("+")-b.count("-")
    if l-f in c:
        print((d[c.index(l-f)])/sum(d))
    else:
        print(0)