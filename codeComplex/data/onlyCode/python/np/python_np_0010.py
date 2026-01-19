
n = int(input())


p = []
for i in range(n):
    la = list(map(float,input().split()))
    p.append(la)

full_bit =  (1<<n) - 1
dp = [0]*(full_bit) + [1]

for i in range(full_bit,0,-1):

    cunt = bin(i)[2:].count('1')
    # print(cunt)
    if cunt == 1 or dp[i] == 0:
        continue

    mul = 1/((cunt*(cunt-1))>>1)

    for x in range(n):
        if (i & (1<<x)) == 0:
            continue
        for y in range(x+1,n):
            if (i & (1<<y)) == 0:
                continue

            dp[i-(1<<y)]+=dp[i]*p[x][y]*mul
            dp[i-(1<<x)]+=dp[i]*p[y][x]*mul

ans = []
for i in range(n):
    ans.append(dp[1<<i])

print(*ans)





