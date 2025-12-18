def bin_pow(num, _pow, module):
    if _pow == 0:
        return 1
    if _pow == 1:
        return num % module
    if _pow % 2 == 1:
        return num * bin_pow(num, _pow - 1, module) % module
    res = bin_pow(num, _pow//2, module)
    return (res * res) % module

x, k = map(int, input().split())

if x == 0:
    print(0)
    exit(0)

mod = 10**9 + 7

__power = bin_pow(2, k, mod)

print((x* __power * 2 + 1 - __power) % mod)
