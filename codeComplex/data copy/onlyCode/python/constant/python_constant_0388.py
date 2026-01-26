from math import inf

a=[0,0]
a[0]=[str(c)for c in list(input().strip()) ]
a[1]=[str(X) for X in list(input().strip())]

an = [-inf,-inf,-inf]
if a[0][0]==a[1][0]=='0':
    an[0]=0
elif  a[0][0]!=a[1][0]:
    an[1]=0
x=0
for i in range(1,len(a[0])) :
  #  print(a[0][i],a[1][i],an,x)
    if an[0]==0:
        if a[0][i]==a[1][i]=='0':
            x+=1

            an=[-inf,0 ,-inf]
        elif a[0][i]!=a[1][i]:
            x+=1
            an=[-inf]*3
        else:
            an = [-inf, -inf, -inf]
    elif an[1]==0:
        if a[0][i]==a[1][i]=='0':
            x+=1
            an=[-inf,-inf ,-inf]
        elif a[0][i]!=a[1][i]:
            pass
        else:
            an=[-inf,-inf ,-inf]
    else:
        if a[0][i]==a[1][i]=='0':

            an=[0,-inf ,-inf]
        elif a[0][i]!=a[1][i]:
            an=[-inf,0,-inf]
        else:
            an=[-inf,-inf ,-inf]


print(x)