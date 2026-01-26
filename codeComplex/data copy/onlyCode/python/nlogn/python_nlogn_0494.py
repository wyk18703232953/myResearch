n,m=map(int,input().split())
o=0
c=0
diff=[]
while n:
    n-=1
    a,b=map(int,input().split())
    diff.append(a-b)
    o+=a
    c+=b
#print(o,c,diff)
if m >=o:
    print(0)
elif m <c:
    print(-1)
else:
    diff.sort(reverse=True)
    nd=o-m
    #print(diff,nd)
    for i in range(len(diff)):
        #print(diff[i])
        nd-=diff[i]
        if nd<=0:
            print(i+1)
            break
    
    