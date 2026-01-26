mod = 10**9 + 7
x, k = list(map(int, input().split()))
if x == 0:
    print(0)
    exit()
ans = (x*pow(2, k+1, mod) - (pow(2, k, mod)-1) + mod)%mod
print(ans)
