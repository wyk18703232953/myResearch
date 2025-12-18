n, k = map(int,input().split())

start = 0
cnt = n
cur = 1

while start <= k:
    start += cur
    cnt -= 1
    cur += 1
    
ans = 0

if start != k:
    while cnt > 0:
        if start == k:
            start += cur
            cur += 1
            cnt -= 1
        ans += (start - k)
        cnt -= (start - k)
        start = k

print(ans)
