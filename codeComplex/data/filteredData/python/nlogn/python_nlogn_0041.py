def main(n):
    # 生成确定性输入：长度为 n 的整数数组 a
    if n <= 0:
        return
    a = [(i % 5) + 1 for i in range(1, n + 1)]

    temp = max(a)
    if len(set(a)) == 1 and a[0] == 1:
        if len(a) > 1:
            result = a[:-1] + [2]

        else:
            result = [2]

    else:
        idx = a.index(temp)
        a[idx] = 1
        a.sort()
        result = a

    # print(*result)
    pass
if __name__ == "__main__":
    main(10)