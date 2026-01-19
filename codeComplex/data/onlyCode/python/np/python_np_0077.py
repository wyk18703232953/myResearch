import math
s1 = input()
s2 = input()
x = 0
y = 0
p = 0
for i in range(len(s1)):
    if s1[i] == '+': x+=1
    elif s1[i] == '-': y+=1
    if s2[i] == '+': x-=1
    elif s2[i] == '-': y-=1
    else: p+=1
if x<0 or y<0:
    print(float(0))
else:
    q = math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
    r = q/math.pow(2,p)
    print(r)
