import math
def cm(n,r):
    i = n - r
    C = (math.factorial(n))/(math.factorial(i)*math.factorial(r))
    return C

s1 = input()
s2 = input()
d1={}
d2={}
d1['+']=0
d1['-']=0
d2['+']=0
d2['-']=0
d2['?']=0
r=0
ans=-1
for c in s1:
    d1[c]+=1
for c in s2:
    d2[c]+=1

np = d1['+']-d2['+']
nn = d1['-']-d2['-']
if np<0 or nn<0:
    ans=0
else:
    n=d2['?']
    r=min(np,nn)
    ans=cm(n,r)
    ans = round(float(ans)/float(math.pow(2,n)),9)
print(ans)