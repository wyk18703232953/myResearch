def main(n):
    # 由 n 决定字符串长度，保证长度至少为 1
    length = max(1, n)

    # 构造一个确定性的字符串：循环使用小写字母
    chars = [chr(ord('a') + (i % 26)) for i in range(length)]
    s = "".join(chars)

    res = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            for f in range(i + 1, len(s)):
                if len(s) >= f + j - i:
                    if s[i:j] == s[f:f + j - i]:
                        res = max(res, j - i)
    return res


if __name__ == "__main__":
    # 示例：以 n = 10 作为输入规模
    result = main(10)
    # print(result)
    pass