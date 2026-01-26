t = int(input())
ans = ''
for j in range(t):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    k = 0
    while a > 0 and b > 0:
        if a >= b:
            k += a // b
            a %= b
        else:
            k += (b // a)
            b %= a
    ans += str(k) + '\n'
print(ans)
