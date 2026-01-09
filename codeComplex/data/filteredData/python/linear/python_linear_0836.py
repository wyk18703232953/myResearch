def main(n):
    # n 作为字符串长度规模，同时：
    # q = n（测试用例数量）
    # 每个用例：
    #   长度 = n
    #   k = n // 2（窗口大小）
    #   字符串模式：循环 "RGB"
    q = n
    results = []

    for _ in range(q):
        length = n
        k = max(1, n // 2)

        # 生成确定性的字符串 S_str，循环 RGB
        pattern = ['R', 'G', 'B']
        S = [pattern[i % 3] for i in range(length)]

        # 映射为 0,1,2
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
            # 初始窗口 [0, k)
            if k > length:
                k = length
            for i in range(k):
                if S[i] % 3 != (mod + i) % 3:
                    SUM += 1

            if SUM < ANS:
                ANS = SUM

            # 滑动窗口
            for i in range(k, length):
                if S[i - k] % 3 != (mod + (i - k)) % 3:
                    SUM -= 1
                if S[i] % 3 != (mod + i) % 3:
                    SUM += 1

                if SUM < ANS:
                    ANS = SUM

        results.append(ANS)

    # 输出所有结果，防止被优化器消掉核心逻辑
    for x in results:
        # print(x)
        pass
if __name__ == "__main__":
    main(10)