def main(n):
    # n 表示序列长度
    if n <= 0:
        n = 1

    # 确定性构造输入：长度为 n 的整数序列
    # 这里使用简单模式：a_i = i
    s = [str(i) for i in range(1, n + 1)]
    i = n  # 原程序里只用到了长度，不依赖具体数值

    l = []
    for j in s:
        if not l or int(j) % 2 != l[-1]:
            l.append(int(j) % 2)

        else:
            l.pop()

    if len(l) < 2:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)