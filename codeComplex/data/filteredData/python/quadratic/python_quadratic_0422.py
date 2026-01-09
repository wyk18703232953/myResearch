def main(n):
    # 为了保持与原程序逻辑一致，我们需要两个关键参数：
    # 字符串长度 n，以及重复次数 k。
    # 这里约定：传入的 n 既控制字符串长度，又确定性地映射出 k。

    if n <= 0:
        return ""

    # 确定性生成 k（至少为 1）
    k = 1 + (n % 7)

    # 确定性生成字符串 s，长度为 n
    # 使用一个周期性模式，避免随机性
    base = "abcd"
    s = "".join(base[i % len(base)] for i in range(n))

    ap = 0
    i = 1
    while i < n:
        if s[:i] == s[-i:]:
            ap = i
        i += 1

    result = s + s[ap:] * (k - 1)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例调用，使用一个固定的 n 以保证可重复性
    main(10)