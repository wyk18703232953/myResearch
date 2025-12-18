str=input()
m=0
n=len(str)
for i in range(n):
    for j in range(i,n+1) :
        if str[i:j] in str[i+1:n] and len(str[i:j])>m:
            m=len(str[i:j])
print(m)