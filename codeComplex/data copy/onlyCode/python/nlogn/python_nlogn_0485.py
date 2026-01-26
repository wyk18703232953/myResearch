def isValid(k):
    last=a[0]
    count=1
    step=0
    i=1
    if count==k and step+1==n:
        return True
    elif count==k:
        step+=1
        count=1
##    print(a)
    while i<m:
##        print(step,i,count,"'''")
##        if i==99:
##            print(a[i],last)
        if step==n:
            return True
        if count==k:
            step+=1
            count=1
            if step==n:
                return True
            last=a[i]
        elif a[i]==last:
            count+=1
##            if i==99:
##                print("Yes",count,step+1,n)
            if count==k and step+1==n:
                return True
        elif a[i]!=last:
            last=a[i]
            count=1
        i+=1
    return False
    
        
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
l=1
h=m
ans=0
##print("t",isValid(1))
##print(a)
while l<=h:
    mid=(l+h)//2
##    print(mid)
    if isValid(mid)==True:
        ans=mid
        l=mid+1
    else:
        h=mid-1
print(ans)
