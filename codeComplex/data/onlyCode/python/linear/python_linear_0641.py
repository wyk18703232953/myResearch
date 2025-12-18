n = int(input())
a = [int(s) for s in input().split()]
os = 0
oss = []
nos = 0
nos_0 = -1
nos_1 = -1
sumnos = 0
for i in range(n):
    if a[i] == 1:
        os += 1
        oss.append(i+1)
    else:
        sumnos += a[i]
        nos += 1
        if nos_0 == -1:
            nos_0 = i+1
        nos_1 = i+1

if os <= sumnos-(2*(nos-1)):
    es = []
    oss_i = 0
    ans = nos-1
    if os >= 1:
        ans += 1
        es.append((nos_0, oss[0]))
        oss_i += 1
    if os >= 2:
        ans += 1
        es.append((nos_1, oss[1]))
        oss_i += 1
    print("YES", ans)
    prev_nos = -1
    for i in range(n):
        if a[i] > 1:
            if prev_nos != -1:
                es.append((prev_nos+1, i+1))
            for j in range(a[i]-2):
                if oss_i >= os:
                    break
                es.append((i+1, oss[oss_i]))
                oss_i += 1
            prev_nos = i
    print(len(es))
    for e in es:
        print(*e)
else:
    print("NO")



