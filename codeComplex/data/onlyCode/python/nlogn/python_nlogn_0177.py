n = int(input())
ls= [list(map(int, input().split())) for i in range(n)]

lsr = [[max(ls[i][0]-ls[i][1], 0), ls[i][0]+ls[i][1]] for i in range(n)]
lsr.sort(key=lambda x: x[1])
idx = 0
ans = 0

for l in lsr:
    if idx <= l[0]:
        idx = l[1]
        ans+=1

print(ans)