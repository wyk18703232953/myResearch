if __name__=="__main__":
    dic={}
    n,m=map(int,input().split())
    li=list(map(int,input().split()))
    c=0
    for i in range(n):
        dic.setdefault(i+1,0)
    for i in li:
        if 0 not in dic.values():
            c=c+1
            for j in range(1,n+1):
                dic[j]=dic[j]-1

        dic[i]=dic[i]+1
    if 0 not in dic.values():
        c=c+1
    print(c)
