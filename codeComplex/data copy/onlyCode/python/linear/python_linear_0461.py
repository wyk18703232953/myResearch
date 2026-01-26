try:
    n,k=list(map(int,input().split(" ")))
    s=input()
    s=list(s)
    if len(s)>k:
        p='('*(k//2)
        p=list(p)
        c=0
        for i in range(0,len(s)):
            if s[i]==')':
                p.insert(i,')')
                c+=1
                if c==k//2:
                    break
        print("".join(p))
                
            
                
    
    else:
        print("".join(s))
    
except:
    pass