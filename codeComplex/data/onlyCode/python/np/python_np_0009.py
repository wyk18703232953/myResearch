x0, y0 = map(int, input().split())
n = int(input())
arr = [[x0, y0]]
for i in range(0, n):
    x, y = map(int, input().split())
    arr.append([x, y])
dist = [[0 for j in range(0, n+1)] for i in range(0, n+1)]
for i in range(0, n+1):
    for j in range(0, n+1):
        dist[i][j] = (arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2

def dfs(status, memo, pp):
    if memo[status] != None:
        return memo[status]
    if status < 0:
        return 1e8
    res = 1e8
    prev = []
    for i in range(1, n+1):
        if (status & (1 << (i - 1))) == 0:
            continue
        t1 = status ^ (1 << (i - 1))
        # print(memo, pp)
        temp = dfs(t1, memo, pp) + dist[0][i]*2
        if temp < res:
            res = temp
            prev = [i, 0]
        for j in range(i+1, n+1):
            if j == i:
                continue
            if (t1 & (1 << (j - 1))) == 0:
                continue
            next = t1 ^ (1 << (j - 1))
            temp = dfs(next, memo, pp) + dist[0][j] + dist[j][i] + dist[i][0]
            if temp < res:
                res = temp
                prev = [i, j, 0]
        break
    memo[status] = res
    pp[status] = prev
    return res


memo = [None for i in range(0, 1 << n)]
pp = [None for i in range(0, 1 << n)]
memo[0] = 0
pp[0] = []
start = 0
end = 0
for i in range(0, n):
    end += (1 << i)
res = dfs(end, memo, pp)
path = [0]
cur = end
while cur > 0:
    prev = pp[cur]
    path.extend(prev)
    for i in range(len(prev) - 1):
        cur -= (1 << (prev[i] - 1))

print(res)
print(' '.join(map(str, path)))



