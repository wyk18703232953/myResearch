def main(n):
    # 将输入规模 n 映射为原程序的两个整数 a[0], a[1]
    # 确定性构造：a0 = n, a1 = 2*n + 1
    a0 = n
    a1 = 2 * n + 1

    # 原逻辑开始
    a = [a0, a1]
    n_val = a[0] ^ a[1]
    x = bin(n_val)[2:]
    f = 0
    first_one_index = 0
    for i in range(len(x)):
        if x[i] == '1':
            f = 1
            first_one_index = i
            break
    l = len(x) - first_one_index
    s = 0
    for i in range(l):
        s += 2 ** i
    if f == 0:
        s = 0
    # print(s)
    pass
if __name__ == "__main__":
    main(10)