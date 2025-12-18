n = int(input())
ans = []
m = 1
while n > 3:
    ans += [m] * (n - n // 2)
    n //= 2
    m *= 2
if n == 3:
    ans += [m, m, m * 3]
elif n == 2:
    ans += [m, m * 2]
else:
    ans += [m]
print(*ans)
