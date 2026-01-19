import math
s1=input()
s2=input()
s1p=s1.count("+")
s1m=s1.count("-")
s2p=s2.count("+")
s2m=s2.count("-")
s2q=0
if '?' in s2:
    s2q=s2.count("?")
if s2q==0:
    if s1p==s2p and s1m==s2m:
        print("%.12f"%1)
    else:
        print("%.12f"%0)
else:
    if s1p>=s2p and s1m>=s2m:
        s2q=math.factorial(s2q)/(math.factorial(s1p-s2p)*math.factorial(s1m-s2m))
        print("%.12f"%(s2q/(2**s2.count("?"))))
    else:
        print("%.12f"%0)
        
    
