import random

def main(n):
    # 生成测试数据：
    # n 行，每行长度 m，允许删除最多 k 个 '1'
    #
    # 为了让规模由 n 控制，这里设：
    #   m = max(1, n // 2)
    #   k = min(m, n // 3)
    # 并随机生成由 '0' 和 '1' 组成的字符串。
    m = max(1, n // 2)
    k = min(m, max(0, n // 3))

    # 随机数据（可以根据需要修改为固定模式）
    rows = []
    for _ in range(n):
        row = ''.join(random.choice('01') for _ in range(m))
        rows.append(row)

    # 原逻辑开始（移除 input，使用生成的 rows, n, m, k）
    dp = [0] * (k + 1)
    l = []
    fk = None

    for s in rows:
        s = list(s)
        d = []
        if list(set(s)) == ['0']:
            d.append(0)
            # 注意：原代码这里 continue 会跳过后面 l.append(d) 等逻辑，
            # 但原代码的缩进实际上是有问题的：
            #     if list(set(s))==['0']:
            #         d.append(0)
            #         continue
            #     one = []
            # 实际行为是：该行被跳过，dp 不更新。
            # 为保持一致，这里也 continue。
            continue

        one = []
        for i in range(len(s)):
            if s[i] == '1':
                one.append(i)

        ni = len(one)
        d = [10**9] * (ni + 1)
        d[-1] = 0
        for i in range(ni):
            for j in range(i, ni):
                d[ni - (j - i + 1)] = min(d[ni - (j - i + 1)], one[j] - one[i] + 1)

        l.append(d)
        fk = [10**9] * (k + 1)
        for i in range(k + 1):
            for j in range(ni + 1):
                if i + j > k:
                    break
                fk[i + j] = min(fk[i + j], dp[i] + d[j])
        dp = fk[:]

    # 输出结果
    print(min(dp))


if __name__ == "__main__":
    # 示例调用，可手动修改 n 测试
    main(10)