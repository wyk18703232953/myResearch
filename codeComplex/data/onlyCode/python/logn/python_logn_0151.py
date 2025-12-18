import decimal

n, k = input().split(' ')
n = int(n)
k = int(k)
coef1 = (k*k-k-2*n)*100+225
if coef1 < 0:
    print('-1')
else:
    D = decimal.Decimal
    coef11 = D(coef1)
    coef1 = coef11.sqrt()
    coef2 = k*10-5
    coef = (coef2-coef1)/10
    if coef % 1 == 0:
        print(int(coef))
    else:
        print(int(coef)+1)
