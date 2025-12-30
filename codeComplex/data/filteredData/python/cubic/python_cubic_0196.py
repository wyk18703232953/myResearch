import random

INF = 10001
mod = int(1e9) + 7


def main(n):
    # 1. 生成测试数据 a，长度为 n
    # 原代码对 a 的取值范围没有限制，这里假设为 [0, 10] 的随机整数
    a = [random.randint(0, 10) for _ in range(n)]

    # 2. 原逻辑
    dp1 = [[0] * n for _ in range(n)]
    dp2 = [[n] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        dp1[i][i] = a[i]
        dp2[i][i] = 1
        for j in range(i + 1, n):
            for k in range(i, j):
                if dp1[i][k] == dp1[k + 1][j] != 0:
                    dp1[i][j] = dp1[i][k] + 1
                    dp2[i][j] = 1
                dp2[i][j] = min(dp2[i][j], dp2[i][k] + dp2[k + 1][j])

    # 3. 返回结果（原程序是输出 dp2[0][n-1]）
    return dp2[0][n - 1]


if __name__ == "__main__":
    # 示例运行：可自行修改 n
    result = main(5)
    print(result)