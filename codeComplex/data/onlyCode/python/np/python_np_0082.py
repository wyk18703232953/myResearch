import math
def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)

s1=input()
s2=input()
ans=0
for i in range(0,len(s1)):
    if(s1[i]=='+'):
        ans+=1
    else:
        ans-=1
t=0
qm=0
for i in range(0,len(s2)):
    if(s2[i]=='+'):
        t+=1
    elif(s2[i]=='-'):
        t-=1
    else:
        qm+=1
if(qm==0):
    if(ans==t):
        print(1.000000000000)
    else:
        print(0.000000000000)
else:
    k=ans-t
    if(abs(k)==qm):
        na=1/pow(2,qm)
        print(na)
    elif(abs(k)>qm):
        print(0.000000000000)
    else:
        if(k%2==0 and qm%2==1):
            print(0.000000000000)
        elif(k%2==1 and qm%2==0):
            print(0.000000000000)
        else:
            a=abs((qm+k)/2)
            b=abs((qm-k)/2)
            nu=factorial(qm)/(factorial(a)*factorial(b))
            ans=nu/(pow(2,qm))
            print(ans)