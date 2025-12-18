st=input()
m=0
n=len(st)
for i in range(n):
    for j in range(i,n+1) :
        if st[i:j] in st[i+1:n] and len(st[i:j])>m:
            m=len(st[i:j])
print(m)