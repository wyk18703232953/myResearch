x,y=map(int,input().strip().split())
if(abs(x-y)<2):
    print(-1)
else:
    k=[]
    for i in range(x,y+1):
        if(i%2==0):
            k.append(i)
            if(i+1<y):
                k.append(i+1)
                k.append(i+2)
                break
    if(len(k)==3):
        print(" ".join(str(t) for t in k))
    else:
        print(-1)