MOD = 10**9 + 7

def solve(a):
    dp = [1]
    n = len(a)
    for i in range(n):
        if a[i] == 'f':
            dp.append(0)
            continue
        for j in range(1, len(dp)):
            dp[j] = (dp[j] + dp[j - 1]) % MOD
    return dp[-1]

def main(n):
    """
    n: 规模，表示指令序列长度
    返回：根据生成的测试数据 a 计算得到的结果
    测试数据规则：前半部分为 'f'，后半部分为 's'
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    # 生成一组确定性的测试数据：
    # 前 half 个是 'f'，后面的为 's'
    half = n // 2
    a = ['f'] * half + ['s'] * (n - half)

    return solve(a)

if __name__ == "__main__":
    # 示例：可以在此处手动调用 main 进行简单测试
    # print(main(5))
    pass