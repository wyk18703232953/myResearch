import random

def main(n):
    # 生成测试数据：长度为 n 的数组 a
    # 这里生成 1~3 的随机整数，可以根据需要修改
    a = [random.randint(1, 3) for _ in range(n)]

    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = [a[i], 1]

    for length in range(1, n):          # 子区间长度 = length + 1
        for j in range(n - length):     # 区间起点 j，终点为 j + length
            v, c = -1, length + 1       # 初始化：值 -1，步数为最大 length + 1
            for k in range(length):     # 切分点
                left_v, left_c = dp[j][j + k]
                right_v, right_c = dp[j + k + 1][j + length]

                if left_v != -1 and left_v == right_v:
                    # 可以合并成一个块，值为 left_v + 1，步数为 1
                    v, c = left_v + 1, 1
                    break
                else:
                    # 不能合并，取最小步数
                    v = -1
                    c = min(c, left_c + right_c)

            dp[j][j + length] = [v, c]

    # 输出结果
    print(dp[0][n - 1][1])


if __name__ == "__main__":
    # 可以修改这里的 n 来测试不同规模
    main(5)