import sys
input=sys.stdin.readline
def read():return list(map(int,input().split()))
n,m=read()
a=[]
for i in range(n):
    a.append(read())
sm=0
cur=0
for x, y in a:
    sm+=y
    cur+=x
if sm>m:
    print(-1)
    quit()
cnt=0
a.sort(key=lambda x: -x[0]+x[1])
i = 0
while cur>m and i < n:
    cur -= a[i][0]-a[i][1]
    cnt += 1
    i += 1
print(cnt)