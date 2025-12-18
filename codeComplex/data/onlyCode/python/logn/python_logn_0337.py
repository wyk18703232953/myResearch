x, k = map(int, input().split())
if x == 0:
    print(0)
else:
    mod = 1000000007
    ans = x * pow(2, k + 1, mod) - pow(2, k, mod) + 1
    print(ans % mod)
