def main(n):
    # n 作为输入规模：生成长度为 n 的字符串列表
    # 构造序列：0, 1, 2, ..., n-1
    s = [str(i) for i in range(n)]

    l = []
    for j in s:
        val = int(j) % 2
        if not l or val != l[-1]:
            l.append(val)

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