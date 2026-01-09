mod, bits = 998244353, ['00', '01', '10', '11']
pat = [[0, 1, 1, 1], [0, 0, 2, 0], [0, 2, 0, 0], [1, 1, 1, 0]]
add = lambda a, b: (a + b) % mod

def main(n):
    # 这里将“规模” n 直接作为原程序中的 n
    # k 根据 n 构造测试数据，这里选择 k = n，保证有一定复杂度
    k = n

    mem = [[[0 for _ in range(4)] for _ in range(k + 1)] for _ in range(n)]

    # 初始化第一个位置
    for i in range(4):
        val = min(bits[i].count('0'), 1) + min(bits[i].count('1'), 1)
        if val <= k:
            mem[0][val][i] = 1

    # DP 转移
    for i in range(1, n):
        for j in range(1, k + 1):
            for k1 in range(4):
                if mem[i - 1][j][k1] == 0:
                    continue
                for k2 in range(4):
                    val = j + pat[k1][k2]
                    if val <= k:
                        mem[i][val][k2] = add(mem[i - 1][j][k1], mem[i][val][k2])

    ans = sum(mem[-1][k]) % mod
    # print(ans)
    pass

# 示例：直接运行文件时给一个默认规模
if __name__ == "__main__":
    main(5)