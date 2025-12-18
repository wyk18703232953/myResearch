from collections import defaultdict

n,k=[int(i) for i in input().strip().split()]
l=[int(i) for i in input().strip().split()]
if(k==1):
    print(n)
else:
    l.sort()
    ndict=defaultdict(list)
    for x in l:
        i=x
        while(i%k==0):
            i=i/k
        ndict[i].append(x)
    ans=0
    for i in ndict.values():
        count=0
        while(count<len(i)):
            if(count==len(i)-1):
                ans+=1
                break
            if(i[count]*k!=i[count+1]):
                ans+=1
                count+=1
            else:
                ans+=1
                count+=2
    print(ans)