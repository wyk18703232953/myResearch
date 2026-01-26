# cook your dish here
n=int(input())
l=[int(x) for x in input().strip().split()]
l1=sorted(l)
c=0
for i in range(n):
    if(l[i]!=l1[i]):
        c+=1
if(c<=2):
    print("YES")
else:
    print("NO")