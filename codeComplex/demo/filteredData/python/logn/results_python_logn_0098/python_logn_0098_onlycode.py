l,r=map(int,input().split())
ls=str(bin(l))[2:]
rs=str(bin(r))[2:]
llog=len(ls)
rlog=len(rs)
ans=0
if llog<rlog:
    z=rlog-1
    while z>-1:
        ans+=2**z
        z-=1
else:
    ct=0
    stringa=""
    for i in range(len(ls)):
        if ls[i]==rs[i] and ct==0:
            stringa+=ls[i]
        if ls[i]=="0" and rs[i]=="1":
            ct+=1
            stringa+=ls[i]
        if ls[i]=="1" and rs[i]=="0":
            stringa+=ls[i]
        if ls[i]==rs[i] and ct>0:
            stringa+=str((int(rs[i])+1)%2)
    ans=(int(stringa,2)^r)
print(ans)