def main(n):
    # 映射含义：
    # N = n（字符串长度）
    # K = max(1, n % 6 + 1)（字母种类数量，1~6 之间变化，随 n 可扩展）
    N = max(1, n)
    K = max(1, n % 6 + 1)

    # 生成确定性的字符串 S，包含小写字母和 '?'
    # 模式：周期为 (K+1)，前 K 个位置是 0..K-1，第 K 个位置是 '?'
    S_list = []
    for i in range(N):
        t = i % (K + 1)
        if t == K:
            S_list.append('?')
        else:
            S_list.append(chr(ord('a') + t))
    S = S_list
    S = [-1 if _ == '?' else ord(_) - ord('a') for _ in S]

    def check(x):
        p = [[N for _ in range(N + 1)] for _ in range(K)]

        for k in range(K):
            keep = 0
            for i in range(N - 1, -1, -1):
                keep += 1
                if S[i] != -1 and S[i] != k:
                    keep = 0
                p[k][i] = p[k][i + 1]
                if keep >= x:
                    p[k][i] = i + x - 1

        d = [N for _ in range(1 << K)]
        d[0] = -1
        for s in range(1, 1 << K):
            base = d[s]
            for k in range(K):
                if (s & (1 << k)) and (d[s ^ (1 << k)] < N):
                    cand = p[k][d[s ^ (1 << k)] + 1]
                    if cand < base:
                        base = cand
            d[s] = base
        return d[(1 << K) - 1] < N

    l, r = 0, N // K if K > 0 else 0
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid):
            l = mid
        else:
            r = mid - 1

    print(l)


if __name__ == "__main__":
    main(1000)