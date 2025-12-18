from math import factorial
s1=input()
s2=input()
n=0
x1=0
for i in range(len(s1)):
    if s1[i]=='+':
        x1+=1
    else:
        x1-=1
x2=0
for i in range(len(s2)):
    if s2[i]=='+':
        x2+=1
    elif s2[i]=='?':
        n+=1
    else:
        x2-=1
x=abs(x1-x2)
if x>n:
    print(0)
elif x==n:
    print(1/2**n)
else:
    if (n-x)%2==1:
        print(0)
    else:
        print((factorial(n)//(factorial((n-x)//2)*factorial(n-(n-x)//2)))/2**n)