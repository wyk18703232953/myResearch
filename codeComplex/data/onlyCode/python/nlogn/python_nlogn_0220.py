N,U = map(int,input().strip().split())

E = list(map(int,input().strip().split()))
maxu = -1
j = 2
if N < 3:
    print(-1)
for i in range(N-2):
    j = max(i+2,j)
    if E[j] -E[i] > U:
        continue
    while j < N and E[j] - E[i] <= U:
        j += 1
    j -= 1
    maxu = max(maxu, (E[j] - E[i+1]) / (E[j] - E[i]))
print(maxu)