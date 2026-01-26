l,r = [int(i) for i in input().split()]
bitafter=-1;
for i in range(60,-1,-1):
    if(l&(1<<i)!=r&(1<<i)):
        bitafter = i
        break
res = 0
while(bitafter>=0):
    res+=1<<bitafter
    bitafter-=1
print(res)