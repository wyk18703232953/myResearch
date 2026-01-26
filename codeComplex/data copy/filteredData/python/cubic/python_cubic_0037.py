def main(n):
    # 生成确定性字符串，长度为 n
    # 使用小写字母循环生成，例如：abcabcabc...
    if n <= 0:
        s = ""

    else:
        chars = [chr(ord('a') + (i % 26)) for i in range(n)]
        s = "".join(chars)

    for i in range(len(s), 0, -1):
        for j in range(len(s) - i + 1):
            if s[j: j + i] in s[j + 1:]:
                # print(i)
                pass
                return
    # print(0)
    pass
if __name__ == "__main__":
    # 示例调用
    main(10)