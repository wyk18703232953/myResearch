import random

def main(n):
    # 生成测试数据：长度为 n 的数组 a，元素为 1~n 之间的整数
    a = [random.randint(1, n) for _ in range(n)]

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
                    break
                dp2[i][j] = min(dp2[i][j], dp2[i][k] + dp2[k + 1][j])

    # 返回结果，若需要打印可改为 print(res)
    return dp2[0][n - 1]


if __name__ == "__main__":
    # 示例：调用 main(5)
    result = main(5)
    print(result)