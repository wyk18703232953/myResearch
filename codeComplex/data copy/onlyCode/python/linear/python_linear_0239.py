n=int(input())
st_a=input()
st_b=input()
st_c=input()
a=[0 for i in range(125)]
b=[0 for i in range(125)]
c=[0 for i in range(125)]
l=len(st_c)
for i in range(l):
    a[ord(st_a[i])] +=1
    b[ord(st_b[i])] +=1
    c[ord(st_c[i])] +=1
maxi_a=0
maxi_b=0
maxi_c=0
if n==1:
    maxi_a =max(a) +1
    maxi_b=max(b) +1
    maxi_c=max(c) +1
    if maxi_a >l:
        maxi_a-=2
    if maxi_b >l:
        maxi_b -=2
    if maxi_c >l:
        maxi_c-=2
else:
    for i in range(123):
        if (i>=65 and i <=90) or (i>=97 and i<=122):
            if a[i] +n >=l:
                    maxi_a=max(maxi_a,l)
            else:
                maxi_a =max(maxi_a ,a[i] +n)
            if b[i] +n >=l:
                    maxi_b=max(maxi_b,l)
            else:
                maxi_b =max(maxi_b ,b[i] +n)
            if c[i] +n >=l:
                    maxi_c=max(maxi_c,l)
            else:
                maxi_c =max(maxi_c ,c[i] +n)
s=[maxi_a,maxi_b,maxi_c]
s.sort()
if s[1] ==s[2]:
    print("Draw")
if maxi_a >max(maxi_b,maxi_c):
    print("Kuro")
if maxi_b >max(maxi_c,maxi_a):
    print("Shiro")
if maxi_c >max(maxi_b,maxi_a):
    print("Katie")
