DV = 10**9 +7

x , k = list(map(int , input().split()))

mult = pow (2, k, DV)
if x == 0:
    print(0)
else:
    print((2*mult*x - mult +1) % DV)
