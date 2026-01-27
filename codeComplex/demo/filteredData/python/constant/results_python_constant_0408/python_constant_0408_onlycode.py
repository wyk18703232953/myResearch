def inn1(s1):
    t=False
    for i in s1:
        if i[0]>=xmi1 and i[0]<=xma1 and i[1]>=ymi1 and i[1]<=yma1:
            t=True
            break
    if c2[0]>=xmi1 and c2[0]<=xma1 and c2[1]>=ymi1 and c2[1]<=yma1:
            t=True
    return t
def inn2(s):
    t=False
    for i in s:
        if i[0]>=xmi2 and i[0]<=xma2 and i[1]>=ymi2 and i[1]<=yma2:
            t=True
            break
    if c1[0]>=xmi2 and c1[0]<=xma2 and c1[1]>=ymi2 and c1[1]<=yma2:
            t=True
    return t
def conv(s):
    for i in range(4):
        x=s[i][0]
        y=s[i][1]
        s[i][0]=x+y
        s[i][1]=x-y
    return s
aux=list(map(int,input().split()))
s=[]
for i in range(0,8,2):
    s.append([aux[i],aux[i+1]])
aux=list(map(int,input().split()))
s1=[]
for i in range(0,8,2):
    s1.append([aux[i],aux[i+1]])
st=set()
for i in s:
    st.add(i[1])
xma1=s[0][0];xma2=s1[0][0];xmi1=s[0][0];xmi2=s1[0][0];yma1=s[0][1];yma2=s1[0][1];ymi1=s[0][1];ymi2=s1[0][1]
for i in range(4):
    xma1=max(xma1,s[i][0])
    xma2=max(xma2,s1[i][0])
    xmi1=min(xmi1,s[i][0])
    xmi2=min(xmi2,s1[i][0])
    yma1=max(yma1,s[i][1])
    yma2=max(yma2,s1[i][1])
    ymi1=min(ymi1,s[i][1])
    ymi2=min(ymi2,s1[i][1])
c1=[(xma1+xmi1)/2,(yma1+ymi1)/2]
c2=[(xma2+xmi2)/2,(yma2+ymi2)/2]
t=False
if len(st)==2:
    t=True
if t:
    t1=inn1(s1)
    s=conv(s)
    s1=conv(s1)
    xma1=s[0][0];xma2=s1[0][0];xmi1=s[0][0];xmi2=s1[0][0];yma1=s[0][1];yma2=s1[0][1];ymi1=s[0][1];ymi2=s1[0][1]
    for i in range(4):
        xma1=max(xma1,s[i][0])
        xma2=max(xma2,s1[i][0])
        xmi1=min(xmi1,s[i][0])
        xmi2=min(xmi2,s1[i][0])
        yma1=max(yma1,s[i][1])
        yma2=max(yma2,s1[i][1])
        ymi1=min(ymi1,s[i][1])
        ymi2=min(ymi2,s1[i][1])
    c1=[(xma1+xmi1)/2,(yma1+ymi1)/2]
    c2=[(xma2+xmi2)/2,(yma2+ymi2)/2]
    t2=inn2(s)
else:
    t1=inn2(s)
    s=conv(s)
    s1=conv(s1)
    xma1=s[0][0];xma2=s1[0][0];xmi1=s[0][0];xmi2=s1[0][0];yma1=s[0][1];yma2=s1[0][1];ymi1=s[0][1];ymi2=s1[0][1]
    for i in range(4):
        xma1=max(xma1,s[i][0])
        xma2=max(xma2,s1[i][0])
        xmi1=min(xmi1,s[i][0])
        xmi2=min(xmi2,s1[i][0])
        yma1=max(yma1,s[i][1])
        yma2=max(yma2,s1[i][1])
        ymi1=min(ymi1,s[i][1])
        ymi2=min(ymi2,s1[i][1])
    c1=[(xma1+xmi1)/2,(yma1+ymi1)/2]
    c2=[(xma2+xmi2)/2,(yma2+ymi2)/2]
    t2=inn1(s1)
    
if t1 or t2:
    print("YES")
else:
    print("NO")
    
