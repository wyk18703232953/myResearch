a=[int(x) for x in input().split()]
n=a[0]^a[1]
x=bin(n)[2:]
#print(x)
f=0
for i in range(len(x)):
    if x[i]=='1':
        f=1
        break
l=len(x)-i
sum=0
for i in range(l):
   sum+=2**i
if f==0:
    sum=0
print(sum)