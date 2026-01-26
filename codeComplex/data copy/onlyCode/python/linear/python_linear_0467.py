import sys
input=sys.stdin.readline
s=list(input().rstrip())
n=len(s)
s.extend(s)
cnt=0
c=1
for i in range(len(s)-1):
  if s[i]!=s[i+1]:
    c+=1
  else:
    cnt=max(c,cnt)
    c=1
cnt=max(cnt,c)
print(min(cnt,n))