n, m = map(int, input().split())
tc = [0]*m
ps = []
for _ in range(n):
    temp = input()
    psa = [0]*m
    for i in range(m):
        if temp[i] == '1':
            psa[i] += 1
            tc[i] += 1
    ps.append(psa)
ans = 'NO'

for i in ps:
    c = 0
    for j in range(m):
        if tc[j]-i[j] > 0:
            c += 1
    if c == m:
        ans = 'YES'
        break

print(ans)
