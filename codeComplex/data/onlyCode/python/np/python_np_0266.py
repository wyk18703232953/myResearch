import math
temp=list(map(int,input().split()))
N,q=temp[0],temp[1]
for j in range(0,q):
    u=int(input())
    S=input()
    k=(N+1)//2
    n=int(math.log((N+1),10)/math.log(2,10))-1
    dup_n=n
    store=[k]
    while u!=k:
        n-=1
        if u>k:
            k+=2**(n)
        else:
            k-=2**(n)
        store.append(k)
    for i in range(0,len(S)):
        if S[i]=='R':
            n-=1
            if n==-1:
                n=0
                continue
            k+=2**(n)
        elif S[i]=='L':
            n-=1
            if n==-1:
                n=0
                continue
            k-=2**(n)
        else:
            if n==dup_n:
                continue
            store.pop()
            k=store[len(store)-1]
            n+=1
            continue
        store.append(k)
            
    print(k)