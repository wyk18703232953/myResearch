n,k = map(int,input().split())
s = input()
f = 0
for i in range(1,n):
    if s[:n-i]==s[i:]:
        f=1
        break
if f==0:
    print(s*k)
else:
    j = n-i
    final = s[j:]
    print(s+final*(k-1))