from math import factorial
s1 = input()
s2 = input()
p = 0
m = 0
blank = 0
for i in range(len(s1)):
    if (s1[i] == "+"):
        p += 1
    else:
        m += 1
    if (s2[i] == "+"):
        p -= 1
    elif (s2[i]=="-"):
        m -= 1
    else:
        blank += 1
if (m<0 or p<0):
    print(0)
else:
    if (m==0):
        print(0.5 ** p)
    elif (p==0):
        print(0.5 ** m)
    else:
        b = blank
        print((factorial(b)/factorial(p)/factorial(m))*(0.5**b))
        
