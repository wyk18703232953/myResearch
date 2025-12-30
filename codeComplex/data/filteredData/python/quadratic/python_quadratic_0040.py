def main(n: int) -> int:
    # 生成测试数据：长度为 n 的指令序列，随机/规则可按需要修改
    # 这里示例为交替 "f" 和 "s"
    c = [" "]
    for i in range(1, n + 1):
        c.append("f" if i % 2 == 0 else "s")

    mod = 10 ** 9 + 7
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

    return sdp[0] % mod


if __name__ == "__main__":
    # 示例调用
    n = 5
    print(main(n))