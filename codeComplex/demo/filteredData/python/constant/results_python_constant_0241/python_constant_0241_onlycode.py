def Fast_power(x , y):
    res = 1
    while y > 0 :
        if (y % 2 != 0):
            res = res * x

        y = y // 2
        x = x * x

    return res

n = int(input())
m = int(input())

if n <= 40 :
    print(m % Fast_power(2 , n))
else:
    print(m)


