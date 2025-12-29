import random

def main(n):
    # 生成测试数据，这里生成 1~3 之间的随机整数
    # 可以根据需要修改数据分布
    global a, dp
    a = [random.randint(1, 3) for _ in range(n)]
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    def solve(l, r):
        if dp[l][r]:
            return dp[l][r]
        if r - l == 1:
            dp[l][r] = (a[l], 1)
            return dp[l][r]
        tmp = 10 ** 9
        for i in range(l + 1, r):
            left = solve(l, i)
            right = solve(i, r)
            if left[0] == -1 or right[0] == -1:
                tmp = min(tmp, left[1] + right[1])
            elif left == right:
                tmp_val = left[0] + 1
                dp[l][r] = (tmp_val, 1)
                return dp[l][r]
            else:
                tmp = min(tmp, 2)
        dp[l][r] = (-1, tmp)
        return dp[l][r]

    solve(0, n)
    print(dp[0][n][1])


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)