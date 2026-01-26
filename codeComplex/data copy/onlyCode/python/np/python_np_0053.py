import math
a=input()
b=input()
c=int(0)
d=int(0)
q=int(0)
for i in range(len(a)):
    if a[i]=="+":
        c+=1
    elif a[i]=="-":
        c-=1
for i in range(len(b)):
    if b[i]=="+":
        d+=1
    elif b[i]=="-":
        d-=1
    else:
        q+=1
if c == d:
    print((math.factorial(q)/(math.factorial(q/2)*math.factorial(q/2)))/(2**q))
else:
    mx=d+q
    mn=d-q
    if c>mx or c<mn:
        print(0.0)
    else:
        ans=c-d
        if ans > 0:
            print((math.factorial(q)/(math.factorial(((q-ans)/2)+ans)*math.factorial((q-ans)/2)))/(2**q))
        else:
            print((math.factorial(q)/(math.factorial((q-ans)/2)*math.factorial(((q-ans)/2)+ans)))/(2**q))