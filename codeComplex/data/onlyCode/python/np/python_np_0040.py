import math
sone= list(input())
stwo = list(input())
sum1=0
sum2=0
m=0
for i in range(len(sone)):
    if sone[i]=='+':
        sum1=sum1 + 1
        m=m+1
    else:
        sum1=sum1 - 1
k=0        
for i in range(len(stwo)):
    if stwo[i]=='+':
        sum2=sum2 + 1
        k=k
    elif stwo[i]=='-':
        sum2=sum2 - 1
        k=k
    elif stwo[i]=='?':
        k=k+1
n=0
if (k-(abs(sum1-sum2)))<0:
    print(float (0))
elif (k-(abs(sum1-sum2)))==0:
    if k==0:
        print(float (1))
    else:
        print(float (pow(0.5,k)))
             
else:
    n=k-(abs(sum1-sum2))
    n=abs(sum1-sum2)+n/2
    if abs(sum1-sum2)==0:
        print(float ((math.factorial(k)/(math.factorial(k/2)*math.factorial(k/2))) * pow(0.5,k)))
    else:
        print(float ((math.factorial(k)/(math.factorial(k-n) * math.factorial(n))) * pow(0.5,k)))