n=input()
n1=int(n)
c=[]
for i in range(0,n1):
    z4=0
    p,q=input().split()
    a=int(p)
    b=int(q)
    while a!=0 and b!=0:
        z1=z3=0
        if a<=b:
          z=(b/a)
          z1=int(z)
          b=b-(z1*a) 
        if b<=a and b!=0:
          z2=a/b
          z3=int(z2)
          a=a-(z3*b) 
        z4=z4+z1+z3    
    c.append(z4)
l=len(c)
for j in range(0,l):
    print(c[j])
    