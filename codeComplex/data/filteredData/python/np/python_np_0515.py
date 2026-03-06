def main(n):
    # 映射规则：
    # N = n（字符串长度）
    # K = 3 固定（保证子集 DP 规模随 K 固定，主要随 N 变化，便于时间复杂度实验）
    # 字符串模式：周期为 3 的循环 'a', 'b', '?'，并在部分位置填充 '?'
    if n <= 0:
        return 0

    K = 3
    N = n
    # 构造确定性的字符串 S：长度 N，字母或 '?'
    # 周期模式：0 -> 'a', 1 -> 'b', 2 -> '?'
    # 额外规则：当 i % 5 == 0 时强制为 '?'，增加不确定位置
    S = []
    for i in range(N):
        if i % 5 == 0:
            S.append(-1)
        else:
            t = i % 3
            if t == 0:
                S.append(0)  # 'a'
            elif t == 1:
                S.append(1)  # 'b'
            else:
                S.append(-1)  # '?'

    II = {1 << i: i for i in range(20)}

    def calc(mmm):
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
                    if i + mmm < mi:
                        mi = i + mmm
                Xk[i] = mi

        Y = [0] * (1 << K)
        for i in range(1, 1 << K):
            mi = inf
            for j in range(K):
                if (i >> j) & 1:
                    ii = i ^ (1 << j)
                    if Y[ii] < N:
                        v = X[j][Y[ii]]
                        if v < mi:
                            mi = v
            Y[i] = mi
        return 1 if Y[-1] < inf else 0

    l, r = 0, N // K + 1
    while r - l > 1:
        m = (l + r) >> 1
        if calc(m):
            l = m
        else:
            r = m

    # 为了时间复杂度实验，返回结果而不是打印
    return l


if __name__ == "__main__":
    # 示例调用：可按需修改 n 的值进行规模实验
    result = main(3000)
    print(result)