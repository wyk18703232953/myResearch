def main(n):
    # 1. 根据规模 n 生成测试数据：这里生成一个长度为 n 的字符串
    #    可以根据需要调整生成规则，这里用周期性模式方便测试最长公共前缀
    import string
    pattern = "abacaba"
    s = "".join(pattern[i % len(pattern)] for i in range(n))

    # 2. 原逻辑：在字符串 s 中，求任意两个起点不同的后缀之间的
    #    最长公共前缀长度（原程序三重循环暴力比较）
    ans = 0
    length = len(s)
    for i in range(length - 1):
        for j in range(i + 1, length):
            # 两个后缀起点分别为 i, j
            # 最长公共前缀不会超过 length - j
            for k in range(length - j):
                if s[i + k] != s[j + k]:
                    break
                if 1 + k > ans:
                    ans = 1 + k

    print(ans)


if __name__ == "__main__":
    # 举例：调用 main(50)。评测时可由外部更改 n。
    main(50)