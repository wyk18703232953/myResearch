import random

def main(n):
    # 根据规模 n 生成测试数据
    # 分成三个数组的长度，使得总长度约为 n，且每个至少为 1
    if n < 3:
        n = 3
    # 随机拆分 n 为三个正整数
    a = random.randint(1, n - 2)
    b = random.randint(1, n - 1 - a)
    c = n - a - b
    x, y, z = a, b, c

    # 生成随机数组，数值范围可自行调整
    arr_x = [random.randint(1, 10**3) for _ in range(x)]
    arr_y = [random.randint(1, 10**3) for _ in range(y)]
    arr_z = [random.randint(1, 10**3) for _ in range(z)]

    # 以下为原逻辑，仅移除 input，并用生成的数组代替
    x += 1
    y += 1
    z += 1

    lengths = [x, y, z]
    arrs = [arr_x, arr_y, arr_z]

    for a_arr in arrs:
        a_arr.sort()

    dp = [[[0 for _ in range(z)] for _ in range(y)] for _ in range(x)]

    for i in range(1, x):
        for j in range(1, y):
            dp[i][j][0] = dp[i - 1][j - 1][0] + arr_x[i - 1] * arr_y[j - 1]

    for j in range(1, y):
        for k in range(1, z):
            dp[0][j][k] = dp[0][j - 1][k - 1] + arr_y[j - 1] * arr_z[k - 1]

    for i in range(1, x):
        for k in range(1, z):
            dp[i][0][k] = dp[i - 1][0][k - 1] + arr_x[i - 1] * arr_z[k - 1]

    for i in range(1, x):
        for j in range(1, y):
            for k in range(1, z):
                opt1 = dp[i - 1][j - 1][k] + arr_x[i - 1] * arr_y[j - 1]
                opt2 = dp[i][j - 1][k - 1] + arr_y[j - 1] * arr_z[k - 1]
                opt3 = dp[i - 1][j][k - 1] + arr_x[i - 1] * arr_z[k - 1]
                dp[i][j][k] = max(opt1, opt2, opt3)

    ans = dp[x - 1][y - 1][z - 1]
    print(ans)


if __name__ == "__main__":
    # 示例：n = 30
    main(30)