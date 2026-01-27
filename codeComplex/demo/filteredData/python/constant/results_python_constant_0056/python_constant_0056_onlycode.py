n=int(input())
li=[]
for i in range(1,n+1):
    if n%i==0:
        li.append(i)
p=0
for t in li:
    l=[m for m in str(t)]
    if set(l)=={'4'} or set(l)=={'7'} or set(l)=={'4','7'}:
        p+=1
if p>0:
    print('YES')
else:
    print('NO')