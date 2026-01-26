def main(n):
    # 生成长度为 n 的确定性字符串
    # 使用循环字符 'a' 到 'z'
    if n <= 0:
        # print(0)
        pass
        return
    chars = [chr(ord('a') + (i % 26)) for i in range(n)]
    st = ''.join(chars)

    m = 0
    length = len(st)
    for i in range(length):
        for j in range(i, length + 1):
            if st[i:j] in st[i + 1:length] and len(st[i:j]) > m:
                m = len(st[i:j])
    # print(m)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)