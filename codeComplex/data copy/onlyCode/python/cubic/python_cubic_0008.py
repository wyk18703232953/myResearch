s=input()
n=len(s)
m=0

for i in range(n-1):
    for j in range(1,n-i):
        if s[i:i+j] in s[i+1:]:
            if j>m:
                m=j

print(m)
    