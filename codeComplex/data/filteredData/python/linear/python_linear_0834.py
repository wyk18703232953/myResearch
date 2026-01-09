def main(n):
    import math

    rgb = 'RGB'

    # 构造确定性测试数据
    # 设测试组数 t = n
    # 第 i 组：长度 len_i = i + 1，窗口 k_i = max(1, (i + 1) // 2)
    # 字符串 s_i 为循环 "RGB" 的前 len_i 个字符
    t = n
    for i in range(t):
        length = i + 1
        k = max(1, length // 2)
        s = "".join(rgb[j % 3] for j in range(length))

        ans = math.inf
        for start in range(3):
            dp = [0] * (length + 1)
            for idx in range(length):
                cur = rgb[(start + idx) % 3]
                dp[idx + 1] = dp[idx] + (s[idx] != cur)
            for idx in range(length - k + 1):
                ans = min(ans, dp[idx + k] - dp[idx])
        # print(ans)
        pass
if __name__ == "__main__":
    main(10)