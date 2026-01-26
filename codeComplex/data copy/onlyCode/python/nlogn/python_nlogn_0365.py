



n,k = map(int,input().split())


t  = list(map(int,input().split()))

t.sort()


f={}

for j in t:
    if j not in f:
        f[j]=1
    else:
        f[j]+=1


p=0
for j in range(n):
    if j<n-1:
        if t[j+1]>t[j] and t[j]+k >= t[j+1]:
            p+=f[t[j]]
    
print(n-p)
