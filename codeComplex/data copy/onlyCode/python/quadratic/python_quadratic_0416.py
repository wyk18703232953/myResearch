import sys
input=sys.stdin.readline
def read():return list(map(int,input().split()))
n,k=read()
s=input()[:-1]
ans=""
for i in range(len(s)+1, 0, -1):
    res=s
    end=s[-i:]
    for j in range(k-1):
        res += end
    cnt=0
    for j in range(len(res)-len(s)+1):
        if res[j:j+len(s)] == s:
            cnt += 1
    if cnt == k:
        ans = res
print(ans)
