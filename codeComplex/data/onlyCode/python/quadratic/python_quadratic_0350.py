import sys
input=sys.stdin.readline
def read():return list(map(int,input().split()))
n=int(input())
s=input()
t=input()
if sorted(s)!=sorted(t):
    print(-1)
    quit()
s=list(s)
t=list(t)
ans=[]
for i in range(n):
    for j in range(i,n-1):
        if s[j+1] == t[i]:
            for k in range(j,i-1,-1):
                ans.append(k+1)
                s[k+1], s[k] = s[k], s[k+1]
            break
print(len(ans))
print(*ans)