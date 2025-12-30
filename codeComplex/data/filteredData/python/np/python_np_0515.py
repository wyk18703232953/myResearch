import random

def main(n: int) -> int:
    # 生成测试数据：
    # 令 K 为 1~min(20, n) 中的一个随机数，N = n
    # 字符串中随机放入 'a'~chr(96+K) 和 '?'。
    if n <= 0:
        return 0

    N = n
    K = min(20, max(1, n // 5))  # 简单设定：随 n 调整 K 的大小
    letters = [chr(97 + i) for i in range(K)]
    S_str = []
    for _ in range(N):
        # 产生一个字符或 '?'
        if random.random() < 0.2:
            S_str.append('?')
        else:
            S_str.append(random.choice(letters))

    # 将原程序逻辑封装为内部函数
    S = [-1 if a == "?" else ord(a) - 97 for a in S_str]

    def calc(mmm: int) -> int:
        inf = 300000
        X = [[0] * N for _ in range(K)]
        for k in range(K):
            Xk = X[k]
            mi = inf
            r = 0
            for i in range(N - 1, -1, -1):
                if S[i] < 0 or S[i] == k:
                    r += 1
                else:
                    r = 0
                if r >= mmm:
                    mi = min(mi, i + mmm)
                Xk[i] = mi

        Y = [0] * (1 << K)
        for i in range(1, 1 << K):
            mi = inf
            for j in range(K):
                if (i >> j) & 1:
                    ii = i ^ (1 << j)
                    if Y[ii] < N:
                        mi = min(mi, X[j][Y[ii]])
            Y[i] = mi
        return 1 if Y[-1] < inf else 0

    # 二分搜索答案
    l, r = 0, N // K + 1
    while r - l > 1:
        m = (l + r) >> 1
        if calc(m):
            l = m
        else:
            r = m

    # 按题意 “输出” 即返回结果
    return l