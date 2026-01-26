x, k = map(int, input().split())

if x == 0:
    print(0)
    exit()

mod = 10 ** 9 + 7

a = ((x % mod) * pow(2, k + 1, mod)) % mod

print((a - (pow(2, k, mod) - 1)) % mod)