MOD = 10**9 + 7

def main(n):
    # 生成确定性的输入：长度为 n 的字符串数组 s，由 "s" 和 "f" 组成
    # 规则：索引 i 上为 "s" 如果 i % 2 == 0，否则为 "f"
    s = ["s" if i % 2 == 0 else "f" for i in range(n)]

    dps = [[0] * (n + 3) for _ in range(n + 1)]
    dpf = [[0] * (n + 3) for _ in range(n + 1)]

    for k in range(n + 1):
        dps[0][k] = 1

    for pos, char in enumerate(s):
        if char == "s":
            for depth in range(pos + 2):
                dps[pos + 1][depth] = (
                    dpf[pos][depth]
                    - dpf[pos][depth - 1]
                    + dps[pos][pos]
                    - dps[pos][depth - 1]
                )
                dps[pos + 1][depth] += dps[pos + 1][depth - 1]
                dps[pos + 1][depth] %= MOD

            for p in range(pos + 2, n + 1):
                dpf[pos + 1][p] += dpf[pos + 1][p - 1]
                dpf[pos + 1][p] %= MOD
        else:
            for depth in range(1, pos + 2):
                dpf[pos + 1][depth] = (
                    dpf[pos][depth - 1]
                    - dpf[pos][depth - 2]
                    + dps[pos][pos]
                    - dps[pos][depth - 2]
                )
                dpf[pos + 1][depth] += dpf[pos + 1][depth - 1]
                dpf[pos + 1][depth] %= MOD

            for p in range(pos + 2, n + 1):
                dpf[pos + 1][p] += dpf[pos + 1][p - 1]
                dpf[pos + 1][p] %= MOD

    ans = dps[n][n] % MOD
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例调用：可以按需修改 n 的大小进行时间复杂度实验
    main(10)