n=int(input())
l1=[]
l2=[]
for _ in range(n):
    l1.append(input())
for _ in range(n):
    l2.append(input())
c=0
for i in range(n):
    if(l1[i]  in l2):
        l2.remove(l1[i])
    else:
        c+=1
#print(l1,l2)
print(c)
        
        

    