x,k=map(int,input().split())
m=10**9+7
print((x*pow(2,k+1,m) -pow(2,k,m) +1) %(m)) if x >0 else print(0)