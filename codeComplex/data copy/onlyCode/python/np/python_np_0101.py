import math
s1=str(input())
s2=str(input())
d1=0;d2=0;n=0
answer=0
for i in s1:
    if i=='+':d1+=1
    else:
        d1-=1
for i in s2:
    if i=='+':d2+=1
    elif i=='?':n+=1
    else:
        d2-=1
if n>=abs(d2-d1):
    y=(n-abs(d1-d2))/2
    if y%1==0:
        answer=math.factorial(n)/math.factorial(n-y)/math.factorial(y)/2**n
print('%.9f'%answer)