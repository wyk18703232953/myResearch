s = input()
s = s*3
n = len(s)
m,curr=1,1
for i in range(n-1):
    if s[i]!=s[i+1]:
        curr+=1
        m=max(curr,m)
    else:
        curr=1
print(min(m,n//3))
