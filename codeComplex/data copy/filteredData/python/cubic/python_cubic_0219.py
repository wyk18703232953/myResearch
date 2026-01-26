def main(n):
    # 将 n 映射为三个颜色数组的规模
    # 这里选择 r = g = b = n，便于时间复杂度实验
    r = n
    g = n
    b = n

    # 确定性生成数据：使用简单算术构造
    red = [i + 1 for i in range(r)]
    green = [(i + 1) * 2 for i in range(g)]
    blue = [(i + 1) * 3 for i in range(b)]

    red.sort()
    green.sort()
    blue.sort()
    red = red[::-1]
    green = green[::-1]
    blue = blue[::-1]

    dp = []
    for i in range(r + 1):
        temp = [[0] * (b + 1) for _ in range(g + 1)]
        dp.append(temp)

    answer = 0

    for i in range(0, r + 1):
        for j in range(0, g + 1):
            for k in range(0, b + 1):
                if i > 0 and j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] + red[i - 1] * green[j - 1])
                if i > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1] + red[i - 1] * blue[k - 1])
                if j > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1] + green[j - 1] * blue[k - 1])

                if dp[i][j][k] > answer:
                    answer = dp[i][j][k]

    # print(answer)
    pass
if __name__ == "__main__":
    main(10)