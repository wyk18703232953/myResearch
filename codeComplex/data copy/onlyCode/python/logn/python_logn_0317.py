x, k = map(int,input().split())
if x == 0:
    print(0)
    exit()
b = pow(2,k,1000000007)  
a = (2*x - 1)%(1000000007)
print((a*b + 1) % 1000000007)