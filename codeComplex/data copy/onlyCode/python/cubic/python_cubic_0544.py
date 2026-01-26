from sys import stdin, stdout
nmbr = lambda: int(input())
lst = lambda: list(map(int, input().split()))

for _ in range(1):#nmbr()):
    sa=sorted(input(), reverse=True)
    na=len(sa)
    sb=input()
    nb=len(sb)
    if nb>na:
        print(''.join(sa))
        continue
    ans=''
    while sa:
        for i in range(len(sa)):
            new=ans+sa[i]+''.join(sorted(sa[:i]+sa[i+1:]))
            if int(new)<=int(sb):
                ans+=sa[i]
                sa.pop(i)
                break
    print(ans)