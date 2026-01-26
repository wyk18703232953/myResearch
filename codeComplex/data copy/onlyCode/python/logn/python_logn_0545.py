k = int(input())
s = k
i = 1
number_digits = 1
while s - (i * (9 * 10 ** (i - 1))) > 0:
    number_digits = number_digits + 1
    s = s - (i * (9 * 10 ** (i - 1)))
    i += 1
v = (s - 1) // number_digits
s = s - v * number_digits
ans = 10 ** (number_digits - 1) + v
ans = str(ans)
fans = ans[s - 1]
print(fans)
