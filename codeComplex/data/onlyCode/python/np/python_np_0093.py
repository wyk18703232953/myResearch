import math as m
a=input()
b=input()
total_sum=0
req_pos=0
unreco=0
for i in a:
    if i=='+':
        total_sum+=1
        req_pos+=1

    elif i=='-':
        total_sum-=1
for i in b:
    if i=='+':
        total_sum-=1
        req_pos-=1

    elif i=='-':
        total_sum+=1
    else:
        unreco+=1
#case 1
if (total_sum==0 and unreco==0):
    print(1.000000000)
elif (abs(total_sum)>unreco or req_pos<0):
    print(0.000000000)
else:
    ans=m.factorial(unreco)/(m.factorial(req_pos)*m.factorial(unreco-req_pos)*(2**unreco))
    print(ans)
    