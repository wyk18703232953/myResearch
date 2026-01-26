def main(n):
    if n <= 0:
        # print(0)
        pass
        return

    # 构造确定性的字符串，周期为 26
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))

    m = 0
    length = len(s)
    for i in range(length):
        for j in range(i, length + 1):
            if s[i:j] in s[i + 1:length] and len(s[i:j]) > m:
                m = len(s[i:j])
    # print(m)
    pass
if __name__ == "__main__":
    main(10)