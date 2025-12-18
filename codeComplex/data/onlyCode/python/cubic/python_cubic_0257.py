def solve(x,y,z):
    global r,g,b,ans
    if (x > r - 1 and y > g - 1) or (x > r - 1 and z > b - 1) or (y > g - 1 and z > b - 1):
        return 0
    if memo[x][y][z] != -1:
        return memo[x][y][z]
    mx = 0
    if x < r and y < g: 
        mx = max(mx,ra[x]*ga[y] + solve(x+1,y+1,z))
    if x < r and z < b:
        mx = max(mx,ra[x]*ba[z] + solve(x+1,y,z+1))
    if y < g and z < b:
        mx = max(mx,ga[y]*ba[z] + solve(x,y+1,z+1))
    ans = max(ans,mx)
    memo[x][y][z] = mx
    return mx

r,g,b = map(int,input().split())
ra = sorted(list(map(int,input().split())),reverse = True)
ga = sorted(list(map(int,input().split())),reverse = True)
ba = sorted(list(map(int,input().split())),reverse = True)

memo = [[[-1 for k in range(205)] for i in range(205)] for j in range(205)]

ans = 0

solve(0,0,0)
print(ans)

