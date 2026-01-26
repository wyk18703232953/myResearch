def main(n):
    # 生成规模为 n 的测试数据：这里用一个长度为 n 的字符串，
    # 由前几个小写字母循环组成，例如 n=10 => "abcabcabca"
    import string
    letters = string.ascii_lowercase
    l = ''.join(letters[i % len(letters)] for i in range(n))

    # 原逻辑开始
    n = len(l)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            p = l[i:j]
            t = len(p)
            x = 0

            for k in range(n):
                if l[k:k + t] == p:
                    x += 1
            if x >= 2:
                ans = max(ans, t)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例运行，可根据需要修改 n
    main(10)