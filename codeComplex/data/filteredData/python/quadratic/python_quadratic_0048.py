MOD = 1000000007

def add(x, j):
    x %= MOD
    j %= MOD
    return (x + j) % MOD

def main(n):
    # 生成测试数据：长度为 n 的指令串，每个元素为 'f' 或 's'
    # 这里简单生成一个周期模式，方便调试和测试
    statements = [('f' if i % 2 == 0 else 's') for i in range(n)]

    temp = [[0 for _ in range(n)] for _ in range(n)]
    earlier = [[0 for _ in range(n)] for _ in range(n)]

    temp[0][0] = 1
    earlier[0][0] = 1

    # 初始化第一行（对应原代码里读完所有 input 后的初始化）
    j = 1
    while j < n:
        temp[0][j] = 0
        earlier[0][j] = temp[0][j] + earlier[0][j - 1]
        j += 1

    i = 1
    while i < n:
        if statements[i - 1] == 'f':
            j = 1
            while j < n:
                temp[i][0] = 0
                earlier[i][0] = 0
                temp[i][j] = temp[i - 1][j - 1]
                earlier[i][j] = add(earlier[i][j - 1], temp[i][j])
                j += 1

        else:
            j = 0
            while j < n:
                if j == 0:
                    temp[i][j] = earlier[i - 1][n - 1]

                else:
                    temp[i][j] = earlier[i - 1][n - 1] - earlier[i - 1][j - 1]
                earlier[i][j] = add(earlier[i][j - 1], temp[i][j])
                j += 1
        i += 1

    ans = 0
    j = 0
    while j < n:
        ans = add(ans, temp[n - 1][j])
        j += 1

    # print(ans % MOD)
    pass

# 示例：直接运行文件时给一个默认规模
if __name__ == "__main__":
    main(5)