def chnge(last,cap,ini=(0,0)):
    for i in range(ini[1],last[1]):
        fin[i][ini[0]:last[0]] = [cap]*(last[0]-ini[0])

x1,y1,x2,y2,x3,y3 = map(int,input().split())
a = (max(x1,y1),[x1,y1],"A")
b = (max(x2,y2),[x2,y2],"B")
c = (max(x3,y3),[x3,y3],"C")
m = max(a[0],b[0],c[0])
fin = [["*" for i in range(m)] for j in range(m)]

if (x1*y1 + x2*y2 + x3*y3)!=m**2:
    print(-1)
else:
    l = sorted([a]+[b]+[c],reverse = True)
    l[0][1].sort(reverse=True)
    chnge(l[0][1],l[0][2])
    ini=[0,l[0][1][1]]
    last = l[1][1]
    if m in [ini[0]+last[0],ini[1]+last[1]] and (ini[0]+last[0]+ini[1]+last[1])<=2*m:
        last = [ini[0]+last[0],ini[1]+last[1]]
    else:
        last = [ini[0] + last[1], ini[1] + last[0]]
    chnge(last,l[1][2],ini)
    chr = l[2][2]
    print(m)
    for i in fin:
        print("".join(i).replace("*",chr))