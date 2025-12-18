x, k = list(map(int,input().split()))
m = 1000000000 +7
if x!=0:
    p1 = x*2 - 1
    p2 = x*2
    p = (p1 + p2)//2
    print((p*pow(2,k,m) + 1)%m)
else:
    print(x*2)

