def main(n):
    # n 表示每个测试用例的字符串长度
    # 构造确定性的多测试用例结构：
    #  - q = n（测试用例数量）
    #  - 每个测试用例：
    #       length = n
    #       k = n//2 + (t % (n//2 + 1))  （1 <= k <= n）
    #       S 为长度为 n 的 RGB 序列，周期性构造
    if n <= 0:
        return

    q = n
    results = []

    for t in range(q):
        length = n
        base_k = n // 2
        k = base_k + (t % (n - base_k if n - base_k > 0 else 1))
        if k > n:
            k = n

        # 构造确定性的字符串 S，长度为 n，周期 RGB
        chars = ['R', 'G', 'B']
        S = [chars[i % 3] for i in range(length)]

        # 原算法逻辑开始
        for i in range(length):
            if S[i] == "R":
                S[i] = 0
            elif S[i] == "G":
                S[i] = 1

            else:
                S[i] = 2

        ANS = 1 << 50

        for mod in range(3):
            SUM = 0
            for i in range(k):
                if S[i] % 3 != (mod + i) % 3:
                    SUM += 1

            if SUM < ANS:
                ANS = SUM

            for i in range(k, length):
                if S[i - k] != (mod + (i - k)) % 3:
                    SUM -= 1
                if S[i] != (mod + i) % 3:
                    SUM += 1
                if SUM < ANS:
                    ANS = SUM

        results.append(ANS)

    # 为了时间复杂度实验，仅输出最后一个测试用例的结果，避免大量 IO 干扰
    if results:
        # print(results[-1])
        pass
if __name__ == "__main__":
    main(10)