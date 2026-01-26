n,k = map(int,input().split())
M = 1000000007
if(n == 0):
    print(0)
else:
    ans = 2*n - 1
    x  =  pow(2,k,M)
    print((((ans * x) % M) + 1) % M)