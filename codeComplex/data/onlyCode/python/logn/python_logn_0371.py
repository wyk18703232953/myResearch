M = 1000000007
x, k  = map(int,input().split())
if x==0:
    print(0)
else:
    print(((pow(2,k+1,M)*x)%M - pow(2,k,M) +1 ) % M)    
