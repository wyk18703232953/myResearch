modulo = 10 ** 9 + 7
x, k = [int(s) for s in input().split()]

if x == 0:
    print(0)
    exit(0)

k2 = pow(2, k, modulo)
ans = (x * k2 * 2 - k2 + 1) % modulo
print(ans)
