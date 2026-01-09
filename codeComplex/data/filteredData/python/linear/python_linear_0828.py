def main(n):
    # n 作为测试组数 Q
    Q = n
    results = []

    for t in range(Q):
        # 构造每组数据的 N, K
        N = 5 * (t + 1)  # N 随测试编号线性增长：5,10,15,...
        K = max(1, (t % N) + 1) if N > 0 else 1
        if K > N:
            K = N

        # 构造字符串 S，周期性 RGB 模式打乱
        base = ['R', 'G', 'B']
        S = ''.join(base[(i + t) % 3] for i in range(N))

        X = [{"R": 0, "G": 1, "B": 2}[s] for s in S]
        mi = K
        for i in range(3):
            d = 0
            for j in range(N):
                if X[j] != (i + j) % 3:
                    d += 1
                if j >= K and X[j - K] != (i + j - K) % 3:
                    d -= 1
                if j >= K - 1:
                    if d < mi:
                        mi = d
        results.append(mi)

    # 为了便于时间复杂度实验，输出所有结果
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)