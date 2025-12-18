x, k = map(int, input().split())
if x == 0:
    print(0)
    exit()
mod = 10**9+7
ans = 1+(2*x-1)*pow(2, k, mod)
print(ans%mod)
