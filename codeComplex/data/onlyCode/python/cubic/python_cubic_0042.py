str=input()
n=len(str)
ans=0
amap={}
def fun():
    global ans
    for strLen in range(n,0,-1):
        mark=0
        for t in range(0,n):
            if t+strLen>n:
                break
            s=str[t:t+strLen]
            if s in amap:
                amap[s]+=1
            else:
                amap[s]=1
            if amap[s]>=2:
                mark=1
                ans=len(s)
                print(ans)
                break
        if mark==1:
            break
fun()
if ans==0:
    print(ans)