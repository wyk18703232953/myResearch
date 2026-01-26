import math
s1 = input().strip()
s2 = input().strip()
ps1 = 0
ms1 = 0
ps2 = 0
ms2 = 0
qs2 = 0
for i in s1:
    if i=='+':
        ps1+=1
    if i=='-':
        ms1+=1
for i in s2:
    if i=='+':
        ps2+=1
    if i=='-':
        ms2+=1
    if i == '?':
        qs2+=1
if ps2<=ps1 and ms2<=ms1:
    print(math.factorial(qs2)/math.factorial(ps1-ps2)/math.factorial(ms1-ms2)*(0.5**qs2))
else:
    print(0.00000000)