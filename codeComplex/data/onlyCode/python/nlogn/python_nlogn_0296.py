from sys import stdin,stdout
nmbr=lambda:int(stdin.readline())
lst=lambda:list(map(int,stdin.readline().split()))
for _ in range(1):
    n=nmbr()
    l=sorted(zip(lst(),range(n)))
    p=0;ans=[0]*(2*n)
    st=[0]*n;ln=0
    s=input()
    for i in range(2*n):
        ch=s[i]
        if ch=='0':
            st[ln]=p
            ans[i]=l[p][1]+1
            ln+=1
            p+=1
        else:
            ans[i]=l[st[ln-1]][1]+1
            ln-=1
    print(*ans)
