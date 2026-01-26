val=10**9
n,m=map(int,input().split())
arr1=[]
for i in range(n):
    x=int(input())
    arr1.append(x)
arr1.append(val)
arr2=[]
ans=val
finalval=0
arr1.sort()
for i in range(m):
    x1,x2,y=map(int,input().split())
    if(x1==1):
        if(x2==val):
            finalval+=1
        else:
            if(len(arr1)>0 and x2>=arr1[0]):
                arr2.append(x2)
arr2.sort()
i=0
j=0
while(i<len(arr1) and j<len(arr2)):
    if(arr1[i]>arr2[j]):
        j+=1
    elif(arr1[i]==arr2[j]):
        temp1=len(arr2)-j
        #print(temp1,'1')
        ans=min(i+temp1,ans)
        i+=1
    else:
        temp1=len(arr2)-j
        #print(temp1,'2')
        ans=min(i+temp1,ans)
        i+=1
    #print(ans+finalval)
ans=min(i,ans)
print(ans+finalval)



