n=2*int(input())
a=list(map(int,input().split()))
z=0
for i in range(0,n-1,2):
    if a[i]!=a[i+1]:
        for j in range(i+1,n):
            if a[j]==a[i]:
                z+=j-i-1
                a.pop(j)
                a.insert(i+1,a[i])
print(z)