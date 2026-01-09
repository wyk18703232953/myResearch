def problem(s, p):
    for i in range(len(p)):
        l = p[:i] + ' '
        r = p[i:] + ' '
        dp = [0] + [None] * i
        for x in s:
            for j in range(i, -1, -1):
                if dp[j] is None:
                    continue
                if l[j] == x:
                    dp[j + 1] = dp[j] if dp[j + 1] is None else max(dp[j], dp[j + 1])
                if r[dp[j]] == x:
                    dp[j] += 1
        if dp[-1] == len(r) - 1:
            return 'YES'
    return 'NO'


def main(n):
    # n 表示测试用例数量和字符串规模
    t = n
    results = []
    for case in range(t):
        # 生成确定性的 s 和 p
        # s 的长度为 n + case，p 的长度为 max(1, n // 2)
        len_s = n + case
        len_p = max(1, n // 2)

        # 生成 s：周期性字母序列
        s = ''.join(chr(ord('a') + (i % 26)) for i in range(len_s))

        # 生成 p：从 s 中取前 len_p 个字符并做一个确定性变换
        base_p = s[:len_p]
        # 将每个字符向后偏移 1（在 a-z 内循环）
        p = ''.join(chr(ord('a') + (ord(c) - ord('a') + 1) % 26) for c in base_p)

        res = problem(s, p)
        results.append(res)

    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)