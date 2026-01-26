for ctr in range(1):
    s=input().strip()
    for l in range(len(s),0,-1):
        k=[]
        for i in range(0,len(s)-l+1):
            k.append(s[i:i+l])
        if len(k)!=len(list(set(k))):
            print(l)
            exit()
    print(0)
    
