try:
    n=int(input())
    x=list(map(int,input().split(" ")))
    x=set(x)
    x=list(x)
    x.sort()
    if len(x)!=1:
        print(x[1])
    else:
        print("NO")
    
        
    
except:
    pass
