def main(n):
    # 映射：将 n 映射为一对 (l, r)，保持 l <= r 且规模随 n 增长
    # 这里构造一个确定性映射：
    # l = n*(n+1)//2
    # r = l + n
    l_val = n * (n + 1) // 2
    r_val = l_val + n

    l = list(bin(l_val)[2:])
    r = list(bin(r_val)[2:])
    if len(l) < len(r):
        l = ['0'] * (len(r) - len(l)) + l

    s = ""
    for i in range(len(r)):
        if l[i] == r[i]:
            s += "0"

        else:
            s += "1" * (len(r) - i)
            break

    # 保持原程序输出行为
    # print(int(s, 2))
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行规模化实验
    main(10)