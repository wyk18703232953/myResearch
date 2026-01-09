def main(n):
    # 生成确定性输入数据：长度为 n 的整数数组
    # 这里选用简单的算术构造：a[i] = (i % 7) + 1
    a = [(i % 7) + 1 for i in range(n)]

    a.sort()
    count = 0
    for i in range(n):
        cur_c = a[i]
        if not cur_c:
            continue
        count += 1
        for j in range(i + 1, n):
            if a[j] % cur_c == 0:
                a[j] = 0
    # print(count)
    pass
if __name__ == "__main__":
    main(10)