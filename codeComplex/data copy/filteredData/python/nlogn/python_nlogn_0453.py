MAXN = 200001

def less_sum(s, m):
    n = len(s)
    a = 0
    b = 0
    res = 0
    last = 0

    # 为了与原代码行为保持一致，保留同样的 count 数组范围
    count = [0 for _ in range(-MAXN, MAXN + 1)]

    count[0] = 1
    x = 0
    last = 1

    for i in range(n):
        if s[i] > m:
            b += 1

        else:
            a += 1
        x = a - b

        if s[i] > m:
            last -= count[x + 1]

        else:
            last += count[x]

        res += last
        count[x] += 1
        last += 1

    return res

def main(n):
    """
    根据规模 n 生成测试数据，并输出原程序的结果。
    可按需修改数据生成逻辑。
    """
    # 生成测试数据：s 为 1..n 的序列，m 为中位数位置的值
    s = list(range(1, n + 1))
    m = (n + 1) // 2

    # 输出与原程序等价的结果
    # print(less_sum(s, m) - less_sum(s, m - 1))
    pass
if __name__ == "__main__":
    # 示例：调用 main，n 可自行修改或在外部导入调用
    main(5)