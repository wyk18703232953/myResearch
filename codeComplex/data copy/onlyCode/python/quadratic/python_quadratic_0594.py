n,m,k=map(int,raw_input().split())#peutêtre très lourd en m
l=list(map(int,raw_input().split()))
ma=0
for deb in range(n-1,n-m-1,-1):
    cumi=0
    scu=0
    for i in range(deb,-1,-1):
        scu+=l[i]
        ma=max(ma,scu-cumi-k)#pour les chieux taille divisibel par k
        if (deb-i+1)%m==0:
            scu-=k
        if scu<cumi:
            cumi=scu

print(ma)
