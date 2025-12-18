


def rotate(li):
    newli = []
    for x in range (0,n):
        newli.append([])
        newli[x] = li[x].copy()

    for x in range (0,n):
        for y in range (0,n):
            newli[x][y] = li[n-1-y][x]
    return newli

def flipV(li):
    newli = []
    for x in range (0,n):
        newli.append([])
        newli[x] = li[x].copy()
    newli.reverse()
    return newli

def flipH(li):
    newli = []
    for x in range (0,n):
        newli.append([])
        newli[x] = li[x].copy()

    for x in range (0,n):
        newli[x].reverse()
    return newli



n = int(input())
#print((s+1)*s//2-s+1)
#print('Ehab' if s%2==1 else 'Mahmoud')

li1, li2, li3, templi = [], [], [], []

for x in range (0,n):
    li1.append([])
    li2.append([])
    li3.append([])
    templi.append([])
    li1[x]=list(input())

for x in range (0,n):
    li2[x]=list(input())

#identical
if ( li1 ==li2 ):
    print('Yes')
    exit()

#flip horizontal
templi = flipH(li2)
if ( li1 ==templi ):
    print('Yes')
    exit()

#flip vertical
templi = flipV(li2)
if ( li1 ==templi ):
    print('Yes')
    exit()

#rotate1
templi = rotate(li2)
if ( li1 ==templi ):
    print('Yes')
    exit()

#rotate2
templi = rotate(templi)
if ( li1 ==templi ):
    print('Yes')
    exit()

#rotate3
templi = rotate(templi)
if ( li1 ==templi ):
    print('Yes')
    exit()

#flip
templi = flipH(li2)
templi = rotate(templi)
if ( li1 ==templi ):
    print('Yes')
    exit()

templi = rotate(templi)
if ( li1 ==templi ):
    print('Yes')
    exit()

templi = rotate(templi)
if ( li1 ==templi ):
    print('Yes')
    exit()

print('No')    
