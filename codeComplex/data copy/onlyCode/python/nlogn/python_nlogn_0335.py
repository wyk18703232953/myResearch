li=[]
for _ in range(int(input())):
    s=input() 
    li.append(s) 
lst2 = sorted(li, key=len) 
c=1 
for i in range(len(lst2)-1):
    if(lst2[i] not in lst2[i+1]):
        c=0 
if(c==1):
    print("YES")
    for j in lst2:
        print(j)
else:
    print("NO")
        