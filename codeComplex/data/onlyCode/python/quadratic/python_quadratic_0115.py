n,m = map(int, input().split())
tL0 = list(map(int, input().split()))
tL = [0] * n
score = 0

for i in range(m):
    tL[tL0[i] - 1] += 1
    if(0 not in tL):
        score += 1
        for i in range(n):
            tL[i] = tL[i] - 1

print(score)