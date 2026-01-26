def binar(a,st,d):
    if st==0:
        return 1
    
    elif st==1:
        return a%d
    
    return (   binar(a**2%d,st//2,d) *  binar(a, st%2,d)   )%d

x,k=map(int,input().split())

if x==0:
	print(0)
	exit()

res= ((x*binar(2,k+1,1000000007)) - (binar(2,k,1000000007))+1)% 1000000007 
print(res)