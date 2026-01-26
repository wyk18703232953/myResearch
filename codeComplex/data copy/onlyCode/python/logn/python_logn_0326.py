mod = 10 ** 9 + 7
x, k = map(int, input().split())
if x != 0:
    print((pow(2, k + 1, mod) * x - pow(2, k, mod) + 1) % mod)
else:
    print(0)

        



