x,k=map(int,input().split())
print(((pow(2,k,1000000007)*((2*x-1)%1000000007))%1000000007+1)%1000000007 if x!=0 else 0)
