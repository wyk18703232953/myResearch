R = lambda :map(int, input().split())
n = int(input())
l = []
for _ in range(n):
    a,b = R()
    l.append((a,-b,_+1))
l = sorted(l)
for i in range(1,n):
    if l[i][1]>=l[i-1][1]:
        print(l[i][2],l[i-1][2])
        break
else:
    print(-1,-1)