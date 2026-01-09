def main(n: int):
    # 根据规模 n 生成测试数据：长度为 n 的只包含 'H' 和 'T' 的字符串
    # 这里给一个简单规则：前一半为 'H'，后一半为 'T'
    s = 'H' * (n // 2) + 'T' * (n - n // 2)

    # 原逻辑开始
    s += s
    h = 0
    for i in range(n):
        if s[i] == 'H':
            h += 1
    ans = h
    for i in range(n):
        c = 0
        for j in range(i, i + h):
            if s[j] == 'T':
                c += 1
        ans = min(ans, c)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)