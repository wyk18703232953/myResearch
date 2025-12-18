games,bills = map(int,input().split())
g = list(map(int,input().split()))
b=list(map(int,input().split()))
total = 0
i=0
j=0

while(i < games and j < bills):
    if g[i] <= b[j]:
        total+=1
        i+=1
        j+=1
    elif g[i] > b[j]:
        i+=1
print(total)