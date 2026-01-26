n, k = map(int, input().split())
grid = [['.']*n for i in range(4)]
if k % 2 == 0:
    for i in range(k//2):
        grid[1][1+i], grid[2][1+i] = '#', '#'
else:
    m = n//2
    if k > n - 2:
        for i in range(1, n-1):
            grid[1][i] = '#'
        for i in range(1, (k-n+2)//2 + 1):
            grid[2][m+i], grid[2][m-i] = '#', '#'
    else:
        grid[1][m] = '#'
        if k > 1:
            for i in range(1, k//2 + 1):
                grid[1][m-i], grid[1][m+i] = '#', '#'
print('YES')
for i in grid:
    print(''.join(i))