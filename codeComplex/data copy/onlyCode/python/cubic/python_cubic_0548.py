import sys
input=sys.stdin.readline
a=list(map(int,input().rstrip()))
b=list(map(int,input().rstrip()))
if len(a)<len(b):
    a.sort(reverse=True)
    print(''.join(map(str,a)))
else:
    ans=-1
    ca=[0]*10
    for aa in a:
        ca[aa]+=1
    lim=-1
    for i in range(len(a)):
        if ca[b[i]]:
            candi=[]
            for j in range(i):
                candi.append(b[j])
            use=-1
            for j in range(b[i]-1,-1,-1):
                if ca[j]:
                    use=j
                    ca[j]-=1
                    candi.append(j)
                    break
            if use<0:
                ca[b[i]]-=1
                continue
            else:
                for j in range(10)[::-1]:
                    candi.extend([j]*ca[j])
                res=''.join(map(str,candi))
                res=int(res)
                ans=max(ans,res)
                ca[use]+=1
                ca[b[i]]-=1
        else:
            candi=[]
            for j in range(i):
                candi.append(b[j])
            use=-1
            for j in range(b[i]-1,-1,-1):
                if ca[j]:
                    use=j
                    ca[j]-=1
                    candi.append(j)
                    break
            if use<0:
                break
            else:
                for j in range(10)[::-1]:
                    candi.extend([j]*ca[j])
                res=''.join(map(str,candi))
                res=int(res)
                ans=max(ans,res)
                ca[use]+=1
                break
    flg=True
    ca=[0]*10
    for i in range(len(a)):
        ca[a[i]]+=1
    for i in range(len(a)):
        if ca[b[i]]:
            ca[b[i]]-=1
        else:
            flg=False
    if flg:
        ans=max(ans,int(''.join(map(str,b))))
    print(ans)