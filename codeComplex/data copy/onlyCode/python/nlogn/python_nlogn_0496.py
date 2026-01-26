n,m = map(int,input().split())
final = []
for i in range(n):
    a,b = map(int,input().split())
    final.append([a,b])
final.sort(key = lambda x: x[0]-x[1])
s1 = 0
s2 = 0
for i in final:
    s2+=i[1]
    s1+=i[0]
if s2>m:
    print(-1)
else:
    if s1<=m:
        print(0)
    else:
        i = n-1
        count = 0
        while s1>m:
            s1 = s1 - (final[i][0]-final[i][1])
            count+=1
            i-=1
        print(count)
