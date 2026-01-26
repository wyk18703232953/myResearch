for _ in range(1):
    i=0
    ans=[]
    while(i<32):
        ans.append(2**i)
        i+=1
        
    
    n=int(input())
    l=list(map(int,input().split()))
    d={}
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
          
    # for j in range(n):
    #     if l[j] in ans1 and d[l[j]]>1:
    #         continue
    #     else:
    #         nl.append(l[j])
    
    
    
    c=0
    for i in d.keys():
        
        for j in ans:
            
            if j-i in d and (j-i!=i or d[j-i]>1):
                
                break
        else:
            c+=d[i]
    print(c)            
                
                
    
    