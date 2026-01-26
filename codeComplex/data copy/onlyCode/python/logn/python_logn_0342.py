
n,k = map(int,input().split(' '))

arr = [n];
k = k+1
z = 1000000007
c = (n*pow(2,k,z)-pow(2,k-1,z)+1)%z
if n==0:
    print(0)
else:
    print(c)

