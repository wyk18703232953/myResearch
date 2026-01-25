def main(n):
    # 映射：对原题中 (n, k, t) 的构造
    # 这里将 k 固定为 n，用于规模化实验；t 为长度 n 的确定性字符串
    if n <= 0:
        return ""
    k = n
    # 构造长度为 n 的确定性字符串 t，由周期 "abc" 生成
    base = "abc"
    t = "".join(base[i % len(base)] for i in range(n))

    # 原 solve 逻辑
    j = 0
    for i in range(1, n):
        if t[:i] == t[-i:]:
            j = i
    s = t + (k - 1) * t[-(n - j):]
    print(s)
    return s


if __name__ == "__main__":
    # 示例调用：可以修改 n 观测不同规模的时间复杂度行为
    main(10)