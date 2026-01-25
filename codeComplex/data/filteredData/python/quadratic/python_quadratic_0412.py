def main(n):
    # 映射：n 为字符串长度，k 固定为 3（可规模化实验）
    if n <= 0:
        return

    k = 3

    # 确定性构造字符串 s，周期性字符序列
    base_chars = "abc"
    s = "".join(base_chars[i % len(base_chars)] for i in range(n))

    ap = 0
    i = 1
    while i < n:
        if s[:i] == s[-i:]:
            ap = i
        i += 1

    result = s + s[ap:] * (k - 1)
    print(result)


if __name__ == "__main__":
    main(10)