def main(n):
    # 生成测试数据：长度为 n 的字符列表，这里简单生成交替字符序列
    # 例如 n=5 -> ['a','b','a','b','a']
    s = [('a' if i % 2 == 0 else 'b') for i in range(n)]

    # 以下为原逻辑
    s = list(s)
    original_n = len(s)
    s.extend(s)
    cnt = 0
    c = 1
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            c += 1
        else:
            cnt = max(c, cnt)
            c = 1
    cnt = max(cnt, c)
    print(min(cnt, original_n))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)