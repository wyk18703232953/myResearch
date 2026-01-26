def main(n):
    # 生成确定性字符串，长度为 n，字符在 'a' 到 'z' 间循环
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))

    m = 0
    length = len(s)
    for i in range(length - 1):
        for j in range(i, length + 1):
            if s[i:j] in s[i + 1:length] and len(s[i:j]) > m:
                m = len(s[i:j])
    # print(m)
    pass
if __name__ == "__main__":
    # 示例调用，可以根据需要修改 n 的值做复杂度实验
    main(100)