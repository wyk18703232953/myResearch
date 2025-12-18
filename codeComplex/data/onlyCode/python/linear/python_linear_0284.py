
op=[0]*1000000
cl=[0]*1000000
def fun(s):
    v = []
    for i in range(len(s)):
        l = len(v)
        if s[i]=='(':
            v.append(s[i])
        elif l>0 and v[l-1]=='(':
            v.pop()
        else :
            v.append(')')
    
    l = len(v)
    if  l==0:
        op[0]+=1
        cl[0]+=1
    elif v[0]==v[l-1]:
        if  v[0]=='(':
            op[l]+=1
        else :
            cl[l]+=1

t = int ( input() )
while t>0:
    t-=1
    s = str ( input() )
    fun(s)
ans = 0
for i in range(1000000):
    ans+=(op[i] * cl[i])

print(ans)