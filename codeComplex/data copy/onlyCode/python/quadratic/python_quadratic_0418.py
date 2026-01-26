n,k=map(int,input().split())
s=input()

i=-1
for j in range(n-1):
    if s[:j+1]==s[n-j-1:]:
        i=j
add=s[i+1:]
for j in range(k-1):
    s+=add
print(s)