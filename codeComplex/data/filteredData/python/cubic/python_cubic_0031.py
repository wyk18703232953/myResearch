def main(n):
    # 生成确定性的字符串，长度为 n
    # 字符集为 'abc' 循环
    s = ''.join(chr(ord('a') + (i % 3)) for i in range(n))

    k = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 2):
            x = s[i:j]
            for t in range(i + 1, len(s)):
                if x == s[t:t + j - i]:
                    k.append(j - i)
    # print(max(k) if k else 0)
    pass
if __name__ == "__main__":
    main(10)