x,k=[int(i) for i in input().split()]
if x!=0:
    print((pow(2,k,1000000007)*(2*x-1)+1)%1000000007)
else:
    print(0)
