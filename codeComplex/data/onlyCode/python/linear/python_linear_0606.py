n = int(input())
ans = [(0, 0)]
for i in range(1, n):
    ans.append((0, i))
    ans.append((i, 0))
    ans.append((0, -i))
    ans.append((-i, 0))
for i in range(n):
    print(str(ans[i][0]) + ' ' + str(ans[i][1]))
