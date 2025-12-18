

n = int(input())


t = list(map(int,input().split()))


t.sort()

if t[-1]==1:
    t[-1]=2
else:
    t[-1]=1
t.sort()
print(*t)
