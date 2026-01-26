n,k = map(int,input().split())
s= input()
s1=s
c=0
for i in range(len(s)-1):
    if(s[:i+1]==s[n-i-1:]):
        c=i+1
for i in range(k-1):
    s1+=s[c:]
print(s1)