l,r = map(int, input().split())
ans = 0
a,b,c = [],[],[]
if l==r:
    print(0)
    exit()

for i in range(63, -1, -1):
    if (r^l) & (1<<i):
        for j in range(i,-1,-1):
            ans|= 1<<j
        break
print(ans)