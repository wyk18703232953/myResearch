import random

def main(n):
    """
    n: 规模，用来控制生成测试数据
    逻辑：原代码是对一个长度为 n 的数组 a 和一个上界 m 进行运算
    这里根据 n 随机生成：
        - m: 整数上界
        - a: 严格递增且位于 [1, m-1] 的长度为 n 的数组
    然后执行原逻辑并打印答案。
    """

    # 1. 生成测试数据
    # 为了保证可行，先生成 m，再生成 a
    # 设 m 至少为 n+2，这样可以在 [1, m-1] 中选出 n 个互不相同的数
    m = max(3, n + 2 + random.randint(0, n))  # m 稍微大于 n

    # 从区间 [1, m-1] 中随机选择 n 个不同的数并排序，形成严格递增序列
    if n >= m - 1:
        # 极端情况下保证可选：直接构造前 n 个
        a = list(range(1, n + 1))
        m = max(m, n + 2)
    else:
        a = sorted(random.sample(range(1, m), n))

    # 2. 原始逻辑（移除 input，改用我们生成的 n, m, a）

    # 在原代码中：a = [0] + a + [m]
    a = [0] + a + [m]
    n2 = len(a)  # 为避免与参数 n 混淆，这里用 n2 表示扩展后的长度

    suf = [0] * n2
    # suf[n2-2] = abs(a[-2] - a[-1])
    suf[n2 - 2] = abs(a[-2] - a[-1])

    # 从后往前计算 suf
    for i in range(n2 - 3, -1, -1):
        suf[i] = a[i + 1] - a[i] + suf[i + 2]

    ans = suf[0]
    cost = 0

    for i in range(1, n2):
        if i & 1:  # 奇数下标
            v = a[i] - 1 - a[i - 1]
            if v != 0:
                ans = max(ans, cost + v + suf[i])
            cost += a[i] - a[i - 1]
        else:       # 偶数下标
            v = a[i - 1] + 1
            if v != a[i]:
                ans = max(
                    ans,
                    cost
                    + a[i] - v
                    + (suf[i + 1] if i + 1 < n2 else 0)
                )

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改或在其他文件中调用 main(n)
    main(5)