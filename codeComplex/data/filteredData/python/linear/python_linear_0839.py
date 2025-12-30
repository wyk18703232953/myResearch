def main(n):
    """
    n: 字符串规模（长度）
    功能：根据规模 n 生成测试数据，运行原逻辑，返回最小修改次数 a
    """
    import random

    # 生成测试数据
    # 原代码一组数据：给定 n, k, s
    # 这里我们根据 n 构造：
    #   k 随机取 [1, n]，s 为长度为 n 的随机 RGB 字符串
    k = random.randint(1, n)
    s = ''.join(random.choice('RGB') for _ in range(n))

    a = 10**9
    ans = [[0] * n for _ in range(3)]
    curr = ['R', 'G', 'B']

    # 预处理：对每种起点模式 l（偏移 0,1,2）
    for l in range(3):
        z = l
        for j in range(n):
            if s[j] != curr[z]:
                ans[l][j] = 1
            z += 1
            z %= 3

    # 前缀和准备，方便区间 [j, j+k-1] 查询
    for i in range(3):
        ans[i] = [0] + ans[i]

    for l in range(3):
        for j in range(1, n + 1):
            ans[l][j] += ans[l][j - 1]

    # 枚举长度为 k 的子串窗口
    for l in range(3):
        for j in range(1, n - k + 2):
            a = min(a, ans[l][j + k - 1] - ans[l][j - 1])

    # 原题是打印答案，这里既打印也返回，方便调试/调用
    print(a)
    return a


if __name__ == "__main__":
    # 示例：调用 main(n) 进行一次测试
    main(10)