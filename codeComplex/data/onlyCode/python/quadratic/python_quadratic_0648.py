n = int(input())
data = [int(i) for i in input().split()]
data.sort()
ans = [0]*n
col = 0
for i in range(n):
    if ans[i] == 0:
        col += 1
        ans[i] = 1
        d = data[i]
        for j in range(i+1, n):
            if data[j] % d == 0:
                ans[j] = 1
print(col)
        
