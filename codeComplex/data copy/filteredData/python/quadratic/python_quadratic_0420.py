def main(n):
    # 映射：n 同时作为字符串长度和重复次数
    length = max(1, n)
    k = max(1, n)

    # 构造一个确定性的字符串 t，包含周期性模式方便算法执行
    # 例如: "abcabcabc..." 截断到指定长度
    base = "abc"
    t = (base * ((length + len(base) - 1) // len(base)))[:length]

    i = 1
    while t[:-i] != t[i:]:
        i += 1
        if i >= len(t):
            break

    # 处理可能找不到这种 i 的情况，保证行为确定
    if i >= len(t):
        i = len(t)

    result = t[:i] * k + t[i:]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例：使用 10 作为规模参数
    main(10)