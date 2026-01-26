n, m = map(int, input().split())
boys = list(map(int, input().split()))
girls = list(map(int, input().split()))
boys.sort(reverse=True)
girls.sort(reverse=True)
s = sum(boys)
ma = max(boys)
#print(s, m)
res = 0
for i in range(0, m):
    #print(girls[i])
    if girls[i] < ma:
        print(-1)
        exit(0)
    res += s
    if (girls[i] == ma):
        girls[i] = 0
j = 0
usage = 0
for i in range(0, m):
    if (usage == m - 1):
        j += 1
    if (j >= n):
        print(-1)
        exit(0)
  #  girls[i] -= max(0, boys[j])
    res += max(0, girls[i] - boys[j])
    usage += 1
print(res)