n,k = map(int, input().strip().split(' '))
lst = list(map(int, input().strip().split(' ')))
s=sum(lst)
s2=0
m=0
for i in range(n-1):
    s2+=lst[i]
    s-=lst[i]
    if (s2%k)+(s%k)>m:
        m=(s2%k)+(s%k)
print(m)
    
    
        
