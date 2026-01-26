n,k=map(int,input().split())
d=(n-k)//2
s=0
while s!=n:
    if (s+1)%(d+1)==0:
        print("1",end="")
    else :
        print("0",end="")
    s+=1
