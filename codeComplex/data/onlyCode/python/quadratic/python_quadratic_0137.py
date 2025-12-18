n=int(input())
pieces=[]
blacks=[0]*4
whites=[0]*4
for i in range(4):
    grid=[]
    for j in range(n):
        grid.append(input())
    if i<3:
        input()
    count=0
    for j in range(n):
        for k in range(n):
            if (int(grid[j][k])+j+k)%2:
                count+=1
    blacks[i]=count
    whites[i]=n*n-count
ans=4*n*n
for white1 in range(3):
    for white2 in range(white1+1,4):
        for black1 in range(4):
            if black1==white1 or black1==white2:
                continue
            for black2 in range(black1+1,4):
                if black2==white1 or black2==white2:
                    continue
                ans=min(ans,whites[white1]+whites[white2]+blacks[black1]+blacks[black2])
print(ans)