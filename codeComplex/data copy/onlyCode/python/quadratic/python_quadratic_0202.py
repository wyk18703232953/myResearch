def fun(grid,counter,n,m):
    for i in range(n):
        possible=True
        for j in range(m):
            if grid[i][j]=='1' and counter[j]==1:
                possible=False
                break
        if possible:
            return True
    return False

n,m=[int(_) for _ in input().split(" ")]
grid,counter=[],[0]*m
for _ in range(n):
    s=input()
    for i in range(m):
        if s[i]=='1':
            counter[i]+=1
    grid.append(s)
if fun(grid,counter,n,m):
    print("YES")
else:
    print("NO")
    
