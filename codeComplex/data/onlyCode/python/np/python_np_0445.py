from sys import stdin


def solve(x: int) -> bool:
    global ans
    dp = {}
    for i in range(n):
        temp = 0
        for j in range(m):
            if a[i][j] >= x:
                temp = temp | (1 << j)
        dp[temp] = i
    for aa, bb in dp.items():
        for cc, dd in dp.items():
            if aa | cc == 2 ** m - 1:
                ans = (bb + 1, dd + 1)
                return True
    return False


ans = (-1, -1)
n, m = map(int, stdin.readline().split())
a = []
for i in range(n):
    a.append(list(map(int, stdin.readline().split())))
l, r = 0, 10 ** 9
while l <= r:
    mid = (l + r) // 2
    if solve(mid):
        l = mid + 1
    else:
        r = mid - 1
print(*ans)
