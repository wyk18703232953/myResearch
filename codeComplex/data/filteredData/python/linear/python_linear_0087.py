def main(n):
    MAX_SIZE = 1000007

    dp = [0] * MAX_SIZE
    majak = [0] * MAX_SIZE

    q = MAX_SIZE
    # 生成确定性的 (a, b) 输入对
    # a 在 [1, 1000002] 中循环分布，b 为 i % 10
    for i in range(n):
        a = 1 + (i % 1000002)
        b = i % 10
        q = min(q, a)
        majak[a] = b

    if q >= 1000003:
        # 若生成导致 q 超出有效范围，则直接输出 n
        # 但正常构造下 q 至多为 1
        # print(n)
        pass
        return

    dp[q] = 1
    ma = 1
    for i in range(q + 1, 1000003):
        if majak[i] == 0:
            dp[i] = dp[i - 1]

        else:
            prev_index = i - majak[i] - 1
            if prev_index >= 0:
                dp[i] = dp[prev_index] + 1

            else:
                dp[i] = 1
            if dp[i] > ma:
                ma = dp[i]

    # print(n - ma)
    pass
if __name__ == "__main__":
    main(100000)