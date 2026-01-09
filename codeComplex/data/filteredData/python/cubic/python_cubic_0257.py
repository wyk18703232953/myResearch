def solve(x, y, z):
    global r, g, b, ans, memo, ra, ga, ba
    if (x > r - 1 and y > g - 1) or (x > r - 1 and z > b - 1) or (y > g - 1 and z > b - 1):
        return 0
    if memo[x][y][z] != -1:
        return memo[x][y][z]
    mx = 0
    if x < r and y < g:
        mx = max(mx, ra[x] * ga[y] + solve(x + 1, y + 1, z))
    if x < r and z < b:
        mx = max(mx, ra[x] * ba[z] + solve(x + 1, y, z + 1))
    if y < g and z < b:
        mx = max(mx, ga[y] * ba[z] + solve(x, y + 1, z + 1))
    ans = max(ans, mx)
    memo[x][y][z] = mx    return mx

def main(n):
    global r, g, b, ans, memo, ra, ga, ba
    r = max(1, n)
    g = max(1, n * 2 // 3)
    b = max(1, n // 2)
    r = min(r, 200)
    g = min(g, 200)
    b = min(b, 200)
    ra = [i + 1 for i in range(r)]
    ga = [2 * (i + 1) for i in range(g)]
    ba = [3 * (i + 1) for i in range(b)]
    ra.sort(reverse=True)
    ga.sort(reverse=True)
    ba.sort(reverse=True)
    memo = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    ans = 0
    solve(0, 0, 0)
    # print(ans)
    pass
if __name__ == "__main__":
    main(50)