n,m = input().split()
n=int(n)
m=int(m)

songs=list()

for i in range(n):
    songs.append([int(c) for c in input().split()])


def sumList(lista,inx):
    sum=0
    for i in range(len(lista)):
        sum+=lista[i][inx]
    return sum

songs=sorted(songs,key=lambda x: x[1]-x[0])


suma = sumList(songs,0)


for i in range(n):
    if(suma<=m):
        print(i)
        exit()
    suma-= songs[i][0]-songs[i][1]

if(suma<=m):
    print(n)
else:
    print(-1)
