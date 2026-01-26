I = lambda: map(int,input().split())
n,l,r,x=I()
C,k=[*I()],0
for i in range(2**n):
    W = [w for w,b in zip(C, bin(i)[2:].zfill(n)) if b=='1']
    
    if l <= sum(W) <= r and max(W)-min(W) >= x:
        k += 1
print(k)