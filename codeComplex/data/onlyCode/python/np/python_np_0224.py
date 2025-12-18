def find(a,b):
    cc=2
    for i in range(1,(1<<len(a))):
        sx=0
        minn=100000000
        maxn=-1
        for j in range(0,len(a)):
            if(i &(1<<j)):
                sx+= a[j];
                minn = min(minn, a[j])
                maxn = max(maxn, a[j])
        if(sx>=b[1] and sx<=b[2] and (maxn-minn)>=b[3]):
            cc+=1
    if(cc<2):
        return 2
    else:
        return cc-2





b=list(map(int,input().split()))
a=list(map(int,input().split()))
print(find(a,b))
