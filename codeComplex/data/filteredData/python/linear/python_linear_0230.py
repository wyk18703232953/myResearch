def main(n):
    # n 表示字符串长度 size
    size = n
    # 确定性构造字符串：周期性地插入 'x'
    # 例如模式：'x','x','x','a','b','c', 重复
    base = ['x', 'x', 'x', 'a', 'b', 'c']
    s_list = [base[i % len(base)] for i in range(size)]
    s = "".join(s_list)

    ct = 0
    F = 0
    for i in range(size - 2):
        if s[i] == s[i + 1] and s[i + 1] == s[i + 2] and s[i] == 'x':
            ct += 1
            F = 1

    if F == 0:
        # print(0)
        pass

    else:
        # print(ct)
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)