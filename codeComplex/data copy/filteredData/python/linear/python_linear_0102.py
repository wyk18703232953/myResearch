def main(n):
    # 生成两个确定性字符串 a 和 b，长度都与 n 相关
    # a: 由小写字母循环构成，长度为 max(1, n)
    # b: 由大写字母循环构成，长度为 max(1, n)
    length = max(1, n)

    a = ''.join(chr(ord('a') + (i % 26)) for i in range(length))
    b = ''.join(chr(ord('A') + (i % 26)) for i in range(length))

    li = []
    for i in range(len(a)):
        li.append(a[:i + 1] + b[0])
    li.sort()
    # print(li[0])
    pass
if __name__ == "__main__":
    main(10)