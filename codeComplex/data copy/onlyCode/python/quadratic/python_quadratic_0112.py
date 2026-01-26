n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(input())
for i in range(n):
    b.append(input())

def h(d):
    c=[]
    for i in range(n):
        c.append(d[n-i-1])
    return c
def r(d):
    c=[]
    for i in range(n):
        temp=""
        for j in range(n):
            temp+=d[j][n-i-1]
        c.append(temp)
    return c
yes=0
for i in range(4):
    if a==b:
        print('YES')
        yes=1
        break
    a=r(a)
if yes==0:
    a=h(a)
    for i in range(4):
        if a==b:
            print('YES')
            yes=1
            break
        a=r(a)
if yes==0:
    print('NO')
    
    