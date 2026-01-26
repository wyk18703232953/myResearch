import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int,input().split()))
c = list(map(int,input().split()))
d = {}
for i in range(n-1):
    ans = 10**12
    for j in range(i+1,n):
        if s[i] < s[j]:
            ans = min(ans,c[i]+c[j])

    d[i] = ans

ans = 10**12
for i in range(n-2):
    for j in range(i+1,n-1):
        if s[i] < s[j]:
            ans = min(ans,c[i]+d[j])

if ans == 10**12:
    print(-1)

else:
    print(ans)