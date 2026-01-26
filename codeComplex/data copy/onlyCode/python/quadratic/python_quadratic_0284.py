n,k=[int(x) for x in input().split()]
lst1=[int(x) for x in input().split()]
lst2=[int(x) for x in input().split()]
lst3={}
ans=[]
for i in lst2:
    if(i in lst1):
        
        lst3[i]=lst1.index(i)
for i in sorted(lst3,key=lst3.get):
    ans.append(i)
#print(lst3)
print(*ans,sep=" ")
