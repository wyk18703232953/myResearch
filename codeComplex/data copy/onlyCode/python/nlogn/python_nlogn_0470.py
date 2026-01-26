n,k=[int(x) for x in input().split(" ")]
a=[int(x) for x in input().split(" ")]
mark,b=[],[]
for x in a:
    b.append(x)
    mark.append(False)
b.sort(reverse=True)
idx,profit=0,0
while idx<k:
    profit+=b[idx]
    for i in range(n):
        if not mark[i] and a[i]==b[idx]:
            mark[i]=True
            break
    idx+=1
print(profit)
prev,counter=-1,0
for i in range(n):
    if counter==(k-1):
        break
    if mark[i]:
        print(i-prev,end=' ')
        prev=i
        counter+=1
print(n-prev-1)
