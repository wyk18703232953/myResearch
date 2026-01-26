def main(n):
    mod = 10 ** 9 + 7

    # 生成确定性的指令序列 c[1..n]，只包含 "f" 和 "s"
    # 规则：下标 i 从 1 开始，若 i 为偶数则 "f"，否则 "s"
    c = [" "] + [("f" if i % 2 == 0 else "s") for i in range(1, n + 1)]

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[1][0] = 1
    sdp = [0] * (n + 1)
    sdp[0] = 1

    for i in range(1, n + 1):
        if i >= 2 and c[i - 1] == "f":
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] % mod
            dp[i][0] = 0

        else:
            for j in range(n + 1):
                dp[i][j] = sdp[j] % mod

        sdp = [dp[i][j] for j in range(n + 1)]
        for j in range(n, 0, -1):
            sdp[j - 1] = (sdp[j - 1] + sdp[j]) % mod

    result = sdp[0] % mod
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例：用不同的 n 调用以做时间复杂度实验
    main(5)