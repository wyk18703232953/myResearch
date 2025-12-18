def cnt(s,t):
    i,c=0,0
    while(s.count(t)):
        s=s[s[i:].index(t)+1:]
        c+=1
    return c
s=(input())
n=len(s)
ln=0
for i in range(n):
    for j in range(i,n):
        if(j-i+1<=ln):
            continue
        if(cnt(s,s[i:j+1])>=2):
            ln=max(ln,j-i+1)
print(ln)
