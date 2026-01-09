def main(n):
    # 这里根据 n 生成测试数据：
    # 约定：k = n，字符串 s 为 "ab" 重复 n 次
    k = n
    s = "ab" * n

    c = 0
    for i in range(len(s) + 1):
        if s[:i] == s[-i:]:
            c = i
    result = s + s[c:] * (k - 1)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)