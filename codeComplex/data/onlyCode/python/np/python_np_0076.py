from math import factorial
f=lambda:input()
a=f()
b=f()
s=0
s1=0
c=0
for i in a:
    if i=='+':
       s+=1
    else:
       s-=1
for i in b:
    if i=='+':
       s1+=1
    elif i=='-':
       s1-=1
    else:
       c+=1
if c==0:
    if s==s1:
        print(c+1)
    else:
        print(c)
else:
    l=[]
    k=c
    i=c
    j=0
    while i>=0:
        l.append(k)
        i-=1
        j+=1
        k=0
        k+=i
        k-=j
    if s1!=0:
        for i in range(len(l)):
            l[i]+=s1
    try:
        c1=l.index(s)
        k=factorial(c)/(factorial(c-c1)*factorial(c1))
        print(k/pow(2,c))
    except:
        print(0.0)