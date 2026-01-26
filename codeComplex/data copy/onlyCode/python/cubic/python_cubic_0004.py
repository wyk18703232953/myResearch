s=input()
m=0
n=len(s)
for i in range(n-1):
    for j in range(i,n+1) :
        if s[i:j] in s[i+1:n] and len(s[i:j])>m:
            m=len(s[i:j])
print(m)