
def aburrimin(x, y, n, m, costder, costaba, dp):
    dists = []
    vals = []
    if x != 0: # izq
        dis = costder[y][x-1]
        dists.append(dis)
        vals.append(dis+dp[y][x-1])
    if y != 0: # arri
        dis = costaba[y-1][x]
        dists.append(dis)
        vals.append(dis+dp[y-1][x])
    if y < n-1: # aba
        dis = costaba[y][x]
        dists.append(dis)
        vals.append(dis+dp[y+1][x])
    if x < m-1: # der
        dis = costder[y][x]
        dists.append(dis)
        vals.append(dis+dp[y][x+1])
    
    mindis = min(dists)
    return min(mindis+dp[y][x],min(vals))
        

def solvecaso():
    n,m,k = map(int,input().split())
    costder = [[int(x) for x in input().split()] for _ in range(n)]
    costaba = [[int(x) for x in input().split()] for _ in range(n-1)]
    if k%2:
        for i in range(n):
            for j in range(m):
                print(-1, end=' ')
            print()
        return -1
    k //= 2
    
    for ren in range(len(costder)):
        for col in range(len(costder[ren])):
            costder[ren][col] *= 2
    for ren in range(len(costaba)):
        for col in range(len(costaba[ren])):
            costaba[ren][col] *= 2
    
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dptemp = [[0 for _ in range(m)] for _ in range(n)]
    # print(dp) # debug
    
    for i in range(k):
        for y in range(n):
            for x in range(m):
                dptemp[y][x] = aburrimin(x, y, n, m, costder, costaba, dp)
        dp, dptemp = dptemp, dp
        # print(dp) # debug
    
    for ren in dp:
        for num in ren:
            print(num, end=' ')
        print()
    
    return 0


if __name__ == "__main__":
    # casos = int(input()) #dbug
    # for caso in range(1,casos+1):#dbug
        # result = solvecaso()#dbug
    solvecaso() #dbug
