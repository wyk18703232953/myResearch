def main(n):
    # 生成长度为 n 的确定性字符串 a 和 b
    # a[i] 为 '0' 或 '1'，模式：奇偶位不同
    a = [('0' if i % 2 == 0 else '1') for i in range(n)]
    # b[i] 为 '0' 或 '1'，模式：整体右移并取反的一种确定性方式
    b = [('1' if (i // 2) % 2 == 0 else '0') for i in range(n)]

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
    # 示例调用，可按需修改 n 测试不同规模
    main(10)