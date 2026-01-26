def mus(x):
    c = 0
    while(x>0):
        c += x%10
        x = x//10
    return c
n,s=map(int,input().split())
ans = s + 10 - s%10
while(ans - mus(ans) < s):
    ans += 10
if ans > n:
    print(0)
else:
    print(n-ans+1)
