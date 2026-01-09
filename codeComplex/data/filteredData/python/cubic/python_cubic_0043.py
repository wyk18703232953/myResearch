def main(n):
    # 生成确定性的字符串作为输入，长度为 n
    # 字符集选择固定的小写字母，按周期重复
    base = "abcdefghijklmnopqrstuvwxyz"
    if n <= 0:
        a = ""

    else:
        a = "".join(base[i % len(base)] for i in range(n))

    l = 0
    for i in range(1, len(a)):
        for j in range(0, len(a) - i + 1):
            t = a.find(a[j:j + i])
            c = a.rfind(a[j:j + i])
            if t != c:
                if i > l:
                    l = i
    # print(l)
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 以做时间复杂度实验
    main(1000)