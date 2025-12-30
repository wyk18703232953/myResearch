def main(n):
    """
    n: 规模，用来生成测试数据
    逻辑：
      - 生成长度为 n 的字符串 s（这里简单生成周期性模式）
      - 生成 k，取值范围 [1, n]（这里令 k = max(1, n // 2)）
      - 按原程序逻辑计算结果字符串并返回
    """
    if n <= 0:
        return ""

    # 生成测试数据
    # s 为长度为 n 的字符串，周期为 3 的模式 'abc'
    base = "abc"
    s = (base * ((n + len(base) - 1) // len(base)))[:n]

    # k 为正整数，随 n 变化
    k = max(1, n // 2)

    # 原始逻辑开始
    fl = 0
    l = None
    for i in range(1, n):
        x = s[i:n]
        for j in range(n):
            if x == s[:j + 1]:
                l = j + 1
                fl = 1
                break
        if fl:
            break

    if fl:
        ans = s + s[l:n] * (k - 1)
    else:
        ans = s * k

    return ans


# 简单自测
if __name__ == "__main__":
    # 示例运行：n = 5
    print(main(5))