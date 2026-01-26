def main(n):
    # 生成确定性字符串：'a', 'ab', 'abc', ...，超过26则循环字母
    if n <= 0:
        s = ""

    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        s = "".join(alphabet[i % 26] for i in range(n))

    for ln in range(len(s), 0, -1):
        for L in range(len(s) - ln + 1):
            if s[L:L + ln] in s[L + 1:]:
                # print(ln)
                pass
                return
    # print(0)
    pass
if __name__ == "__main__":
    # 示例调用
    main(10)