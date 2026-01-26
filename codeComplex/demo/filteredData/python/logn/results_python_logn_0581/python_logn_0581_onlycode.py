import math
k = int(input())


def cnt_digit_order(X):
    res = 0
    if X == 0:
        return 0
    for i in range(1, X+1):
        res += i*(9*pow(10, i-1))
    return res


L = -1
leftcnt = 0
for length in range(1, 100):
    if cnt_digit_order(length - 1) < k <= cnt_digit_order(length):
        L = length
        leftcnt = k - cnt_digit_order(length - 1)
        break

#L = digits/length
M = str(math.ceil(leftcnt/L) + (10**(L-1) - 1))
leftcnt -= 1
leftcnt %= L
print(M[leftcnt])
