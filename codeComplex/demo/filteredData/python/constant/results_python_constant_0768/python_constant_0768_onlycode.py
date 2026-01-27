def find(n,k):
    x=9+8*(n+k)
    a=(-3+int(x**0.5))//2
    b=n-a
    return b
n,k=list(map(int,input().strip().split(' ')))
print(find(n,k))