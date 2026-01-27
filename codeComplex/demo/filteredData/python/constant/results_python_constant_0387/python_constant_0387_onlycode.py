def f(ch):
    if ch=='0':
        return 0
    else:
        return 1

U=[ [f(i) for i in list(input())],
    [f(i) for i in list(input())]]
i=0
size=len(U[0])
ans=0
while i+1<size:
    if U[0][i]+U[0][i+1]+U[1][i]+U[1][i+1]>1:
        i+=1
        continue
    elif U[0][i]+U[0][i+1]+U[1][i]+U[1][i+1]==1:
        U[0][i]=1
        U[0][i+1]=1
        U[1][i]=1
        U[1][i+1]=1
        ans+=1
    else:
        U[0][i]=1
        U[0][i+1]=1
        U[1][i]=1
        ans+=1
    ###
    ###
    ###
    i+=1

print(ans)
