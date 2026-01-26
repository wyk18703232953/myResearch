def main(n):
    from collections import Counter

    # 映射规则：
    # n -> 字符串长度
    # k = min(26, max(1, n % 26 + 1))
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    k = min(26, max(1, n % 26 + 1))

    # 生成确定性字符串 s，长度为 n，在前 k 个字母中循环
    if n <= 0:
        s = ""

    else:
        s = ''.join(alpha[i % k] for i in range(n))

    c = Counter(s)
    mn = 10 ** 9
    for ch in alpha[:k]:
        mn = min(mn, c[ch])
    result = mn * k
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例：以 n = 100 作为输入规模调用
    main(100)