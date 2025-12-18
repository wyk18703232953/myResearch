N, MOD = map(int, input().split())
dp = [[0]*(N+2) for i in range(N+2)]
dp[0][0] = 1
limit = 1000
frac = [1]*limit
for i in range(2,limit):
    frac[i] = i * frac[i-1]%MOD
fraci = [None]*limit
fraci[-1] = pow(frac[-1], MOD -2, MOD)
for i in range(-2, -limit-1, -1):
    fraci[i] = fraci[i+1] * (limit + i + 1) % MOD
bb = [1, 2]
for i in range(1000):
    bb.append(bb[-1] *2 %MOD)
for ln in range(N+1):
    for cnt in range(ln//2, ln+1):
        for k in range(1, N-ln+1):
            cmb = frac[cnt+k] * (fraci[cnt]*fraci[k]%MOD)%MOD
            dp[ln+k+1][cnt+k] += dp[ln][cnt] * (bb[k-1] * cmb % MOD) %MOD
            dp[ln+k+1][cnt+k] %= MOD
R = 0
for x in dp[N+1][:N+1]:
    R = (R+x)%MOD
print(R)
