n=int(input())
a=sorted([int(x) for x in input().split()])
counter=0
test=[False]*n
for j in range(n):
    if not test[j]:
        for i in range(n):
            if not test[i] and a[i]%a[j]==0:
                test[i]=True
        counter+=1
print(counter)
            
