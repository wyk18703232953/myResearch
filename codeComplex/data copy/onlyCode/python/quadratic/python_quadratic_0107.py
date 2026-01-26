def rotate_90(a):
    b=[]
    for x in range(len(a)):
        l=[]
        for y in range(len(a)-1,-1,-1):
            l.append(a[y][x])
        b.append(l)
    return b
def flip(a):
    b=[]
    for x in range(len(a)):
        l=[]
        for y in range(len(a)-1,-1,-1):
            l.append(a[x][y])
        b.append(l)
    return b
n=int(input())
l=[]
for i in range(n):
    a=input()
    l2=[]
    for i2 in a:
        l2.append(i2)
    l.append(l2)
l2=[]
for i in range(n):
    a=input()
    l3=[]
    for i2 in a:
        l3.append(i2)
    l2.append(l3)
d='no'
for i in range(4):
    l = rotate_90(l)
    if l==l2:
        d='yes'
l=flip(l)
for i in range(4):
    l = rotate_90(l)
    if l==l2:
        d='yes'
print(d)
