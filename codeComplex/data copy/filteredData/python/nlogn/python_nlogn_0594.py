def main(n):
    # 映射含义：
    # n -> 原程序中的 n，数组长度
    # k -> 固定设为 0（因为原程序中 k 未被使用）
    k = 0

    # 生成确定性数组 a，长度为 n
    # 例如：a[i] = (i * 2 + 3) // 1
    a = [(i * 2 + 3) for i in range(n)]

    # 原始算法逻辑
    a.sort(reverse=True)
    worst = 0
    maxi = a[0] if n > 0 else 0
    a.append(0)
    for i in range(n + 1):
        bad = maxi - a[i] - i
        worst = max(worst, bad)
    result = sum(a) - n - worst

    # print(result)
    pass
if __name__ == "__main__":
    main(10)