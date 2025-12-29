MOD = 10**9 + 7

def main(n: int) -> None:
    # 生成测试数据：第1行是行数，其余n-1行在'f'和's'之间交替
    # 原程序第一行是行数，之后每行首字符是指令类型
    # 这里保持相同逻辑，只是数据由n生成
    lines = n

    # 特判：原代码会访问 dp[0]，至少需要1行
    if lines <= 0:
        print(0)
        return

    dp = [0] * lines
    f = 1
    dp[0] = 1

    for i in range(lines):
        # 测试数据策略：
        # 偶数行（从0开始）使用'f'，奇数行使用's'
        # 你可以根据需要调整生成规则
        if i % 2 == 0:
            char_in = 'f'
        else:
            char_in = 's'

        if char_in == 'f':
            f += 1
        else:
            for j in range(1, f):
                dp[j] = (dp[j] + dp[j - 1]) % MOD

    print(dp[f - 1])


if __name__ == "__main__":
    # 示例：运行时可以自行修改n来做简单测试
    main(5)