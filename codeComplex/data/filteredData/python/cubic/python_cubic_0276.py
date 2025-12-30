import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据
    # 为了与原题约束兼容，r,g,b 都不超过 200
    n = max(1, min(n, 200))
    r = random.randint(1, n)
    g = random.randint(1, n)
    b = random.randint(1, n)

    # 随机生成颜色数组，元素范围可自行调整
    R = [0] + [random.randint(1, 10**4) for _ in range(r)]
    G = [0] + [random.randint(1, 10**4) for _ in range(g)]
    B = [0] + [random.randint(1, 10**4) for _ in range(b)]

    # 2. 按原代码逻辑进行排序
    R.sort()
    G.sort()
    B.sort()

    # 3. DP 数组：三维 201x201x201，初始化为 0
    # 与原始代码一致，容量固定为 201
    dp = [[[0] * 201 for _ in range(201)] for _ in range(201)]

    # 4. 状态转移
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                x = dp[i - 1][j - 1][k] + R[i] * G[j] if i * j else 0
                y = dp[i][j - 1][k - 1] + G[j] * B[k] if j * k else 0
                z = dp[i - 1][j][k - 1] + R[i] * B[k] if i * k else 0
                dp[i][j][k] = max(dp[i][j][k], x, y, z)

    # 5. 输出结果
    print(dp[r][g][b])


if __name__ == "__main__":
    # 示例：调用 main(50)，可根据需要修改 n
    main(50)