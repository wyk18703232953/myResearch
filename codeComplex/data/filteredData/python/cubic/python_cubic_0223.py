import random

def main(n: int):
    # 生成测试数据规模：
    # 三种颜色数量分别为 n，n，n
    R = G = B = n

    # 随机生成正整数权值（可根据需要修改范围）
    r = [random.randint(1, 10**3) for _ in range(R)]
    g = [random.randint(1, 10**3) for _ in range(G)]
    b = [random.randint(1, 10**3) for _ in range(B)]

    # 原逻辑开始
    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    r = [0] + r
    g = [0] + g
    b = [0] + b

    R += 1
    G += 1
    B += 1

    dp = [[[0] * B for _ in range(G)] for __ in range(R)]
    res = 0

    for i in range(R):
        for j in range(G):
            for k in range(B):
                tmp = 0
                if i > 0 and j > 0:
                    tmp = max(tmp, dp[i - 1][j - 1][k] + r[i] * g[j])
                if i > 0 and k > 0:
                    tmp = max(tmp, dp[i - 1][j][k - 1] + r[i] * b[k])
                if j > 0 and k > 0:
                    tmp = max(tmp, dp[i][j - 1][k - 1] + g[j] * b[k])
                dp[i][j][k] = tmp
                if tmp > res:
                    res = tmp

    print(res)


if __name__ == "__main__":
    # 示例：运行规模 n=3
    main(3)