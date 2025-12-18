list1=input()
l=list1.split()
l=[int(item) for item in l]

n,m,k=l

a=input()
a1=map(int,a.split())

a1=list(sorted(a1))

count=0
for i in range(len(a1)):
    if k>=m:
        break
    else:
        k+=a1.pop()-1
        count+=1

if k>=m:    
    print(count)
else:
    print("-1")