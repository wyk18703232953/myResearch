def main(n):
    # 生成确定性的输入数据
    # a 和 b 为长度为 n 的字符列表，由简单算术规则生成
    a = [('a' if i % 2 == 0 else 'b') for i in range(n)]
    b = [('b' if (i // 2) % 2 == 0 else 'a') for i in range(n)]

    ans = 0
    i = 0
    while i < n:
        if a[i] != b[i]:
            ans += 1
            if i < n - 1 and a[i] == b[i + 1] and b[i] == a[i + 1]:
                i += 1
        i += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)