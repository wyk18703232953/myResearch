from math import factorial
from decimal import *
A=input()
B=input()
a=0
cnt2=0
cnt1=0
b=0
for i in A:
    if i=='+':
        a+=1
        cnt1+=1
    else:
        a-=1
        cnt2+=1
cnt3=0
cnt=0
cnt4=0
for i in B:
    if i=='+':
        b+=1
        cnt3+=1
    elif i=='-':
        b-=1
        cnt4+=1
    else:
        cnt+=1
if cnt3>cnt1 or cnt4>cnt2:
    print(format(0,'.12f'))
else:
    No_of_plus=cnt1-cnt3
    No_of_minus=cnt2-cnt4
    Total_cases=2**cnt
    Total_No_of_favourable_cases=factorial(cnt)//(factorial(No_of_plus)*factorial(No_of_minus))
#     getcontext().prec=12
    print(format(Decimal(Total_No_of_favourable_cases)/Decimal(Total_cases), '.12f'))
    