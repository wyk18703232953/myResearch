def main(n, k):
    # 生成测试数据：用前 n 个小写字母循环构造字符串
    from string import ascii_lowercase
    base = ascii_lowercase
    s = ''.join(base[i % len(base)] for i in range(n))

    f = 0
    for i in range(1, n):
        if s[:n - i] == s[i:]:
            f = 1
            break

    if f == 0:
        print(s * k)
    else:
        j = n - i
        final = s[j:]
        print(s + final * (k - 1))


if __name__ == "__main__":
    # 示例：n=5, k=3，可按需修改
    main(5, 3)