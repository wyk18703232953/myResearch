def main(n):
    # n 表示列表长度
    if n <= 0:
        # print("YES")
        pass
        return

    # 确定性生成 n 个整数，以 i 的平方构造
    s = [str((i * i) % 10) for i in range(1, n + 1)]

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