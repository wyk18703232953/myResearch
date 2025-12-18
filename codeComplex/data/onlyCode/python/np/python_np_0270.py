def lvl(val):
    tot=1
    curr=-1
    while(val%tot==0):
        curr+=1
        tot*=2
    return [curr,val*2//(tot),tot//2]









n,q=map(int,input().split())
for _ in range(q):
    curr=int(input())
    l,v,pw=lvl(curr)
    s=input()
    for j in s:

        if j=="U":
            if v%4==3:
                curr=curr-pw
            else:
                if curr+pw<=n:
                    curr=curr+pw

        elif j=="R":
            if l>0:
                curr=curr+pw//2

        elif j == "L":
            if l > 0:
                curr = curr - pw // 2

        l, v, pw = lvl(curr)

    print(curr)



