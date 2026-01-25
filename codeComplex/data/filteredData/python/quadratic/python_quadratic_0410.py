def main(n):
    # 映射：n -> 字符串长度 = n, k = n（保证可规模化）
    if n <= 0:
        return ""
    k = n
    # 生成确定性字符串：重复 'abc' 模式，长度为 n
    base = "abc"
    s = "".join(base[i % len(base)] for i in range(n))

    c = 0
    for i in range(len(s) + 1):
        if s[:i] == s[-i:] or i == 0:
            c = i
    result = s + s[c:] * (k - 1)
    print(result)
    return result

if __name__ == "__main__":
    main(5)