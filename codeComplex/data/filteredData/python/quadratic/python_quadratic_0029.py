MOD = int(1e9 + 7)

def main(n: int) -> int:
    """
    n: 规模（行数）
    自动生成长度为 n 的序列 a，其中元素为 'f' 或 's'。
    这里给出一个确定性的生成方式，便于测试和复现。
    返回原程序应输出的结果。
    """
    # 生成测试数据：周期性地在序列中放入 'f' 和 's'
    # 例如：['f', 's', 's', 'f', 's', 's', ...]
    a = [('f' if i % 3 == 0 else 's') for i in range(n)]

    dp = [1]
    for i in range(n):
        if a[i] == 'f':
            dp.append(0)
            continue
        for j in range(1, len(dp)):
            dp[j] = (dp[j] + dp[j - 1]) % MOD
    return dp[-1]

if __name__ == "__main__":
    # 示例：调用 main(5) 并打印结果
    # print(main(5))
    pass