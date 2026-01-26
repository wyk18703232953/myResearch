def palin(s):
    if s[::-1] != s or len(s) == 0:
        return len(s)

    else:
        return palin(s[1:])

def main(n):
    # 生成一个确定性的字符串：
    # 前 n 个小写字母循环，如 n=1 -> "a", n=2 -> "ab", ..., n=27 -> "abcdefghijklmnopqrstuvwxyz" + "a"
    if n <= 0:
        s = ""

    else:
        letters = "abcdefghijklmnopqrstuvwxyz"
        s = "".join(letters[i % 26] for i in range(n))
    result = palin(s)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以做规模实验
    main(10)