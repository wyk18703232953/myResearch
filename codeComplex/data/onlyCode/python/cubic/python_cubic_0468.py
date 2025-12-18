def roll(i,j):
    ways = []
    if j:
        ways.append(2*hor[i][j-1] + grid[i][j-1])
    if m-1-j:
        ways.append(2*hor[i][j] + grid[i][j+1])
    if i:
        ways.append(2*ver[i-1][j] + grid[i-1][j])
    if n-1-i:
        ways.append(2*ver[i][j] + grid[i+1][j])
    return min(ways)

n , m , k = map(int, input().split())
hor = [list(map(int, input().split())) for _ in range(n)]
ver = [list(map(int, input().split())) for _ in range(n-1)]


grid = [[0]*m for _ in range(n)]
if k%2:
    for _ in range(n):
        print(" ".join(["-1"]*m))
else:
    for _ in range(k//2):
        new_grid = [[roll(i,j) for j in range(m)] for i in range(n)]
        grid = new_grid[:]
    for i in range(n):
        print(" ".join(map(str,grid[i])))