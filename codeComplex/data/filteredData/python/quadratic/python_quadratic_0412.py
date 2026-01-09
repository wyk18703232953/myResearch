def main(n: int):
    # 这里根据 n 生成测试数据：构造一个有前后缀重合结构的字符串
    # 示例：s = "abcab" * (n // 5) + "abc" 之类，也可以更简单
    # 为了可控，这里生成周期串 "abc" 重复，长度为 n
    base = "abc"
    s = (base * ((n + len(base) - 1) // len(base)))[:n]

    # 这里固定 k 的取值或者按 n 派生一个 k
    # 举例：k = 3（重复 3 次）
    k = 3

    ap = 0
    i = 1
    while i < n:
        if s[:i] == s[-i:]:
            ap = i
        i += 1

    # print(s + s[ap:] * (k - 1))
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(10)