def main(n):
    # 对应原程序的输入结构：两段字符串 s1, s2
    # 将 n 映射为字符串长度规模：len(s1) = n, len(s2) = n
    if n <= 0:
        # print("")
        pass
        return

    # 确定性生成 s1, s2：由下标构造的字符序列
    # 字符集选择 10 个字符循环，保证可扩展
    chars = "abcdefghij"
    s1 = "".join(chars[i % len(chars)] for i in range(n))
    s2 = "".join(chars[(i * 2) % len(chars)] for i in range(n))

    output = s1 + s2
    for j in range(len(s1)):
        s = s1[:j + 1]
        for k in range(len(s2)):
            s += s2[k]
            if sorted([s, output])[0] == s:
                output = s
    # print(output)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以进行规模实验
    main(5)