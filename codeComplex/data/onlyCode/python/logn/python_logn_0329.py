n,k=[int(i) for i in raw_input().split()]


M=10**9+7
def power(x,y):
    if y==0:
      return 1
    z=(power(x,y/2)**2)%M
    z=(z*x)%M if y%2 else z
    return z%M

z=(((2*n-1+M)%M)*power(2,k)+1)%M if n!=0 else 0
print(z)
