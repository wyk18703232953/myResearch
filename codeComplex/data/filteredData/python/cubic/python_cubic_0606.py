import random

def main(n):
    # 依据规模 n 构造参数与测试数据
    # 这里约定：
    #   行数 = n
    #   列数 m = n（可按需要调整策略）
    #   允许删除的 '1' 总数 k = n // 2（也可调整）
    m = n
    k = n // 2

    # 生成随机 0/1 矩阵 table，大小为 n 行 m 列
    # 为了尽量有一些 '1'，按 0.4 的概率放置 '1'
    table = []
    for _ in range(n):
        row = ''.join('1' if random.random() < 0.4 else '0' for _ in range(m))
        table.append(row)

    # 以下是原始逻辑，仅移除 input() 并封装到 main 中
    dp = [0] * (k + 1)

    for a in table:
        one = []
        for i in range(m):
            if a[i] == '1':
                one.append(i)

        if not one:
            continue

        ni = len(one)
        subdp = [10 ** 9] * (ni + 1)
        subdp[-1] = 0

        for i in range(ni):
            for j in range(i, ni):
                subdp[ni - (j - i + 1)] = min(subdp[ni - (j - i + 1)], one[j] - one[i] + 1)

        next_dp = [10 ** 9] * (k + 1)
        for i in range(k, -1, -1):
            for j in range(ni + 1):
                if i + j > k:
                    break
                next_dp[i + j] = min(next_dp[i + j], dp[i] + subdp[j])

        dp = next_dp

    print(min(dp))


if __name__ == "__main__":
    # 示例：以 n = 5 运行
    main(5)