def main(n):
    # 生成确定性输入字符串，长度为 n
    # 使用小写字母周期重复：'abc...zabc...'
    if n <= 0:
        string = ""

    else:
        string = "".join(chr(ord('a') + (i % 26)) for i in range(n))

    totalmax = 0
    for x in range(len(string)):
        curr = ""
        for y in string[x:]:
            curr += y
            if string[x:].rfind(curr) != string[x:].find(curr):
                totalmax = max(totalmax, len(curr))
                continue
    # print(totalmax)
    pass
    return totalmax


if __name__ == "__main__":
    # 示例：使用 n = 100 作为输入规模
    main(100)