n,m = list(map(int,input().split()))
l = []
for i in range(n) :
    s = input()
    l.append(s)
x1=0
x2=0
y1=0
y2=0
for i in range (n) :
    for j in range(m) :
        if l[i][j]=='B' :
            if x1==0 and y1==0 :
                x1,y1 = [i+1,j+1]
            else :
                x2,y2 = [i+1,j+1]
res = []
x=0
y=0
if x2!=0 :
    x = (x2 - x1) // 2
    y = (y2 - y1) // 2
res.append(x1+x)
res.append(y1+y)
print(*res)