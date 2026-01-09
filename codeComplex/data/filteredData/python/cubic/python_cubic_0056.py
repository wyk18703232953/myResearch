def main(n):
    # 生成长度为 n 的确定性字符串
    # 使用小写字母循环构造，如 n=1 -> "a", n=2 -> "ab", ..., n=27 -> "abcdefghijklmnopqrstuvwxyzb"
    if n <= 0:
        s = ""

    else:
        s = "".join(chr(ord('a') + (i % 26)) for i in range(n))

    # 保持原始算法逻辑：寻找最长重复子串长度
    for ln in range(len(s), 0, -1):
        for L in range(len(s) - ln + 1):
            if s[L:L + ln] in s[L + 1:]:
                # print(ln)
                pass
                return
    # print(0)
    pass
if __name__ == "__main__":
    # 示例调用，使用 n=100 作为默认规模
    main(100)