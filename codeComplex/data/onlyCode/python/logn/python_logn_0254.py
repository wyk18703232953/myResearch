x, k = list(map(int,input().split()))
m = 10**9 + 7
if x==0:
    print(0)
else:
    print((pow(2,k+1,m)*x - pow(2,k,m)+1) % m)