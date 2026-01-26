def main(n):
    # 生成一个确定性的长度为 n 的字符串，周期为 3
    # 字符串元素来自固定集合 ['a', 'b', 'c']
    if n <= 0:
        # print(0)
        pass
        return
    base_chars = ['a', 'b', 'c']
    s = ''.join(base_chars[i % 3] for i in range(n))

    # 原始逻辑开始
    s = s + s
    length = len(s)
    an = 1
    m = 1

    for i in range(1, length):
        if s[i] != s[i - 1]:
            m += 1
            an = max(an, m)

        else:
            an = max(an, m)
            m = 1

    # print(min(an, length // 2))
    pass
if __name__ == "__main__":
    main(10)