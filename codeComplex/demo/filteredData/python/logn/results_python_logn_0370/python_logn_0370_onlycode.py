x, k = map(int, input().split())

if x==0:
    print(0)
    exit()
    
MOD = 10**9+7
ans = (pow(2, k+1, MOD)*x%MOD-(pow(2, k, MOD)-1))%MOD

print(ans)