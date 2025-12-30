maxnum = 1005
mod = 1000000007

# 预处理 f[i]: 将 i 变为 1 需要的“1 的个数变换”步数
def preprocess_f(maxnum):
    f = [0] * maxnum

    def cntone(num):
        return bin(num).count('1')

    for i in range(1, maxnum):
        if i == 1:
            f[i] = 0
        else:
            f[i] = f[cntone(i)] + 1
    return f

# 预处理组合数 c[i][j]
def preprocess_c(maxnum, mod):
    c = [[0] * maxnum for _ in range(maxnum)]
    for i in range(maxnum):
        c[i][0] = 1
        for j in range(1, i + 1):
            if j == i:
                c[i][j] = 1
            else:
                c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod
    return c

f = preprocess_f(maxnum)
c = preprocess_c(maxnum, mod)

def main(n):
    """
    使用规模参数 n 生成测试数据并执行原逻辑。
    这里将原先由 input() 读取的 s0 和 k 替换为基于 n 的测试数据：
    - s0: 长度为 n 的二进制串（这里示例为前 half 位为 '1'，后面为 '0'）
    - k : 取为 n // 2
    """
    # 生成测试数据
    if n <= 0:
        return 0

    # 生成一个长度为 n 的二进制字符串 s0
    half = n // 2
    s0 = '1' * half + '0' * (n - half)

    k = max(0, n // 2)

    # 原逻辑开始
    s1 = s0[::-1]
    lens1 = len(s1)

    dp = [[0] * maxnum for _ in range(maxnum)]

    for i in range(lens1):
        if i == 0:
            dp[i][0] = 1
            if s1[i] == '1':
                dp[i][1] = 1
            else:
                dp[i][1] = 0
        else:
            for j in range(0, i + 2):
                if j == 0:
                    dp[i][j] = 1
                    continue
                if s1[i] == '1':
                    dp[i][j] = (dp[i - 1][j - 1] + c[i][j]) % mod
                else:
                    dp[i][j] = dp[i - 1][j] % mod

    ans = 0
    for i in range(1, lens1 + 1):
        if f[i] == k - 1:
            ans = (ans + dp[lens1 - 1][i]) % mod

    if k == 0:
        ans = 1
    elif k == 1:
        ans -= 1

    # 与原程序一样，仅输出最终结果
    print(ans % mod)

if __name__ == "__main__":
    # 示例：调用 main(n)，n 为规模参数
    main(10)