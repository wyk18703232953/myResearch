def main(n):
    # 构造一个长度为 n 的确定性字符串
    # 使用小写字母循环: 'a'..'z'
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))

    m = {}

    def podstroka(s: str):
        for i in range(0, len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if sub in m:
                    m[sub] += 1

                else:
                    m[sub] = 1
        return m

    podstroka(s)

    maxlen = 0
    for x in m:
        if m[x] >= 2 and len(x) > maxlen:
            maxlen = len(x)
    # print(maxlen)
    pass
if __name__ == "__main__":
    # 示例：以 n = 10 作为输入规模
    main(10)