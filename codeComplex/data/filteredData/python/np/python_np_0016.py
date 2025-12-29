import random

def main(n):
    # 1. 生成测试数据 prob：n x n 的概率矩阵，每行和为 1
    prob = []
    for _ in range(n):
        row = [random.random() for _ in range(n)]
        s = sum(row)
        row = [x / s for x in row]
        prob.append(row)

    dp = [-1.0 for _ in range(1 << n)]
    ans = [0.0 for _ in range(n)]

    def move(mask, die):
        total = bin(mask).count('1')
        z = 0.0
        for i in range(n):
            if mask & (1 << i):
                z += prob[i][die]
        return z / ((total * (total - 1)) >> 1)

    def solve(mask):
        if mask == (1 << n) - 1:
            return 1.0
        if dp[mask] != -1.0:
            return dp[mask]
        res = 0.0
        for i in range(n):
            if not (mask & (1 << i)):
                prev = solve(mask ^ (1 << i))
                res += prev * move(mask ^ (1 << i), i)
        dp[mask] = res
        return res

    for i in range(n):
        ans[i] = '%.6f' % solve(1 << i)

    print(*ans)


if __name__ == '__main__':
    # 示例调用：可根据需要修改 n
    main(4)