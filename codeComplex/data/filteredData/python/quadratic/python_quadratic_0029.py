MOD = int(1e9+7)

def main(n):
    # 生成长度为 n 的确定性指令序列 a，由 'f' 和 's' 组成
    # 规则：索引 i 上为 'f' 若 i 是 3 的倍数，否则为 's'
    a = ['f' if i % 3 == 0 else 's' for i in range(n)]

    dp = [1]
    for i in range(n):
        if a[i] == 'f':
            dp.append(0)
            continue
        for j in range(1, len(dp)):
            dp[j] = (dp[j] + dp[j-1]) % MOD
    print(dp[-1])

if __name__ == "__main__":
    # 示例：使用规模 n = 10 运行
    main(10)