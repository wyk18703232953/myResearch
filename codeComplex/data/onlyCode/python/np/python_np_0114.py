from math import factorial
s1,s2=input(),input()
a=s1.count('+')-s2.count('+')
b=s1.count('-')-s2.count('-')
if(a<0 or b<0):
    print(0)
    exit(0)
ans=factorial(a+b)/factorial(a)/factorial(b)
ans/=(2**(a+b))
print("%.10f"%ans)
