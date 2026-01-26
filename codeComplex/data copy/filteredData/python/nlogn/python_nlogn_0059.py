def main(n):
    # n 表示列表长度
    # 生成一个确定性的整数列表，元素值与索引相关
    l = [(i * 2 + 1) % (2 * n + 1) for i in range(n)]
    l = sorted(l)
    s = 0
    c = 0
    cnt = 0
    for i in l:
        s += i
    for i in l[::-1]:
        c += i
        cnt += 1
        if c > (s / 2):
            break
    # print(cnt)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)